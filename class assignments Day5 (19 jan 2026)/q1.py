# Base Class
class Vehicle:
    # Class variable to track number of vehicles created
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")


# Derived Class (Single Inheritance)
class Car(Vehicle):
    def start(self):
        print("Car is starting")


# Multilevel Inheritance
class ElectricCar(Car):
    def start(self):
        print("Electric Car is starting silently")


# Creating objects
v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

# Calling methods
v1.start()
c1.start()
e1.start()

# Display total number of vehicles created
print("Total vehicles created:", Vehicle.vehicle_count)
