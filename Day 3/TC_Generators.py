def generatorex():
    yield 1
    yield 6
    yield 3
gen=generatorex()
print(next(gen))
print(next(gen))
print(next(gen))

def count_up(n):
    for i in range(1,n+1):
        yield i
for val in count_up(5):
    print(val)
print(list(count_up(5)))