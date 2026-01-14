class iteratorclass:
    def __init__(self,limit):
        self.limit=limit
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            val=self.current
            self.current+=1
            return val
        else:
            raise StopIteration
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
print("For loop using Iterator")
num=iteratorclass(10)
for i in num:
    print(i)
print("For loop using Generator")
num=fibonacci(10)
for i in num:
    print(i)