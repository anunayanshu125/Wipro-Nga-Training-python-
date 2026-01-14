
def add(a,b):
    print(a+b)
add(5,6)
def sub(a,b):
    return a-b,a
print(sub(5,4))
def mul(a,b):
    return a*b
print(mul(5,4))

def hello(greeting="hello",name="world"):
    print('%s %s'%(greeting,name))
hello()
hello('good morning','dear')

def print_params(*param):
    print(param)
print_params('testing')
print_params(1,2,3,4,5)
def print_param1(**param):
    print(param)
print_param1(a=1,b=2,c=3)