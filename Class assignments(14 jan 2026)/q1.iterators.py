#1. Create a custom iterator class that iterates over numbers from 1 to N
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

n=int(input("enter n value"))
count=iteratorclass(n)
print(list(count))