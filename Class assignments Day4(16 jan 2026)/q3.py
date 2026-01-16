class Vehicle:
    vehicle_count=0
    def __init__(self,name):
        self.name=name
        Vehicle.vehicle_count+=1
    def start(self):
        print("this is the base class and vehicle is=",self.name)
class Car(Vehicle):
    def starting(self):
        print("this is the starting class")
class Model(Car):
    def Honda(self):
        print("this is the Honda class")
v=Vehicle("Generic")
v.start()

m=Model(name="Honda")

m.starting()
m.Honda()
print("total number of vehicles=",Vehicle.vehicle_count)