#lambda args:Expression
add=lambda a,b:a+b
print(add(3,5))
multi=lambda c,d:c*d
print(multi(100,200))

#multiple Arguments
maxnum=lambda x,y:x if x>y else y
print(maxnum(10,40))

#map(function,iterable)
#map with lambda = function applied ot all the numbers
numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))