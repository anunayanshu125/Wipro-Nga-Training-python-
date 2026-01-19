from abc import ABC, abstractmethod
import json, csv, time
from functools import wraps

class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if not all(0 <= m <= 100 for m in value):
            raise ValueError("Error: Marks should be between 0 and 100")
        instance._marks = value


class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance._salary = value


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIME] {func.__name__} executed in {time.time() - start:.5f}s")
        return result
    return wrapper


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("admin", False):
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper


class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Destructor called for {self.name}")


class Employee(Person):
    def __init__(self, pid, name, department):
        super().__init__(pid, name, department)

class Faculty(Employee):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}\nRole: Faculty\nDepartment: {self.department}"


class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        return f"Name: {self.name}\nRole: Student\nDepartment: {self.department}"

    @logger
    @timer
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        return iter([self.code, self.name, self.credits])

def student_generator(students):
    print("Fetching Student Records...")
    for s in students.values():
        yield f"{s.id} - {s.name}"

class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.faculty = {}
        self.courses = {}

    def add_student(self, student):
        if student.id in self.students:
            raise ValueError("Error: Student ID already exists")
        self.students[student.id] = student
        print("Student Created Successfully")

    def add_faculty(self, faculty):
        self.faculty[faculty.id] = faculty
        print("Faculty Created Successfully")

    def add_course(self, course):
        self.courses[course.code] = course
        print("Course Added Successfully")

    def enroll_student(self, sid, course_code):
        self.students[sid].courses.append(self.courses[course_code])
        print("Enrollment Successful")

    @admin_only
    def generate_reports(self, admin=False):
        with open("students_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
            for s in self.students.values():
                avg, grade = s.calculate_performance()
                writer.writerow([s.id, s.name, s.department, avg, grade])
        print("CSV Report generated successfully")

        with open("students.json", "w") as f:
            json.dump(
                [{"id": s.id, "name": s.name, "department": s.department,
                  "semester": s.semester, "marks": s.marks}
                 for s in self.students.values()],
                f, indent=4
            )
        print("Student data successfully saved to students.json")

def show_menu():
    print("""
1 → Add Student
2 → Add Faculty
3 → Add Course
4 → Enroll Student to Course
5 → Calculate Student Performance
6 → Compare Two Students
7 → Generate Reports
8 → Exit
""")


uni = UniversitySystem()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            s = Student(
                input("Student ID: "),
                input("Name: "),
                input("Department: "),
                int(input("Semester: ")),
                list(map(int, input("Enter 5 marks: ").split()))
            )
            uni.add_student(s)

        elif choice == "2":
            f = Faculty(
                input("Faculty ID: "),
                input("Name: "),
                input("Department: "),
                int(input("Monthly Salary: "))
            )
            uni.add_faculty(f)

        elif choice == "3":
            c = Course(
                input("Course Code: "),
                input("Course Name: "),
                int(input("Credits: ")),
                uni.faculty[input("Faculty ID: ")]
            )
            uni.add_course(c)

        elif choice == "4":
            uni.enroll_student(
                input("Student ID: "),
                input("Course Code: ")
            )

        elif choice == "5":
            sid = input("Student ID: ")
            avg, grade = uni.students[sid].calculate_performance()
            print(f"Average: {avg}\nGrade: {grade}")

        elif choice == "6":
            s1 = uni.students[input("First Student ID: ")]
            s2 = uni.students[input("Second Student ID: ")]
            print(f"{s1.name} > {s2.name} :", s1 > s2)

        elif choice == "7":
            uni.generate_reports(admin=True)

            print("\nStudent Record Generator")
            for record in student_generator(uni.students):
                print(record)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print(e)
