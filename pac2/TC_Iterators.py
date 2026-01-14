data=[2,4,5,8]
it=iter(data)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

class count:
    def __init__(self,limit):
        self.limit=limit
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            values=self.current
            self.current+=1
            return values
        else:
            raise StopIteration
object=count(3)
for num in object:
    print(num)

print("\nList Conversion:")
print(list(count(5)))