def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
fib=fibonacci(10)
print(list(fib))