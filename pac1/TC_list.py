numbers=[10,20,30,40]
names=["Ram","Hari","Ramya"]
mixed=[1,"python",3,5,True]

numbers[1]=100
print(numbers)
print(names)
print(mixed)

print(numbers[0])
print(numbers[1:3])

for i in numbers:
    print(i)
if 10 in numbers:
    print("Found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

print(names.reverse())

names.reverse()
print(names)
names.append("Harika")
print(names)

names.extend(["lakshmi","Mounika"])
print(names)

names.remove("Harika")
print(names)

names.insert(3,"Anu")
print(names)