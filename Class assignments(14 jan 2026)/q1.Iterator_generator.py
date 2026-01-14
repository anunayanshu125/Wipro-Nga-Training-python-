2.1
class PositiveSalary:
    """Descriptor that ensures salary is always a positive number"""

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")

        if value < 0:
            raise ValueError("Salary cannot be negative")

        setattr(obj, self.private_name, value)

2.2
class Employee:
    """Employee class using descriptor for salary validation"""

    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

2.3
# Demonstration
if __name__ == "__main__":
    print("=== Creating Employee objects ===")

    # Create valid employees
    emp1 = Employee("Anunay", 50000)
    emp2 = Employee("Bunny", 75000)
    emp3 = Employee("Champ", 100000)

    print(f"Created: {emp1}")
    print(f"Created: {emp2}")
    print(f"Created: {emp3}")
    print()

    # Test updating salaries
    print("=== Testing salary updates ===")
    emp1.salary = 55000
    print(f"Anunay's new salary: {emp1.salary}")
    print()

    # Test negative salary (should raise ValueError)
    print("=== Testing negative salary ===")
    try:
        emp2.salary = -1000
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test non-numeric salary (should raise TypeError)
    print("=== Testing non-numeric salary ===")
    try:
        emp3.salary = "not_a_number"
    except TypeError as e:
        print(f"Error: {e}")

    print()
    print("=== Final employee details ===")
    print(emp1)
    print(emp2)
    print(emp3)