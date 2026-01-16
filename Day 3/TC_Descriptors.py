class SalaryDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("_salary")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance.__dict__["_salary"] = value

class Employee:
    salary=SalaryDescriptor()
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"Employee Name: {self.name}, salary: {self.salary} "


# Creating valid Employee objects
emp1 = Employee("Anunay", 50000)
emp2 = Employee("anshu", 55000)

print(emp1)
print(emp2)

# Attempting to assign a negative salary
try:
    emp3 = Employee("Anshal", -30000)
except ValueError as e:
    print("Error:", e)