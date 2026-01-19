#Same method name, different behaviors
class Animals:
    def pet(self):
        print("Pet animal")
class Dog:
    def pet(self):
        print("Dog is a pet animal")
class Cat(Dog):
    def pet(self):
        print("Cat is a pet animal")
class Lion(Dog):
    def pet(self):
        print("lion is not a pet animal")
obj=[Dog(),Cat(),Lion()]
for a in obj:
    a.pet()