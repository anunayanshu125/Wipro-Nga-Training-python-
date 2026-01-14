try:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a/b)
except ZeroDivisionError:
    print("division by zero")


try:
    x=int(input("enter x value"))
    print(10/x)
except ValueError:
    print("Invalid entry")
except ZeroDivisionError:
    print("division by zero. can't divide by zero")
else:
    print("Code executed successfully")
