class num:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value
num1=num(2)
num2=num(3)
#result=num1+num2
print(num1+num2)