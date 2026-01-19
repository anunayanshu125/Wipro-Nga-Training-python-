class Calculator:
    def add(self,a,b):
        return a+b
class AdvancedCalculator(Calculator):
    def add(self,a,b):
        return a+b
obj1=Calculator()
obj2=AdvancedCalculator()
print(obj1.add(11,10))
print(obj2.add(24,11))





