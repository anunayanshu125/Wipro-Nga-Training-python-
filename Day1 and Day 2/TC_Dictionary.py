students={"age":18,"marks":75.5,"name":"ramu","sid":101}
print(students)
print(students["age"])
print(students.get("marks"))
students["marks"]=78 #changes marks from 75.5 to 78
print(students)
students.pop("age") #deletes age
print(students)
students.popitem() #deletes last key value pair
print(students)
print(students.keys()) #gives all the keys
print(students.values()) #gives all the values of dictionary
for key in students:
    print(key, students[key])
if "name" in students:
    print("Key Exists")

#nested dictionaries
employees={
    101:{"name":"anunay","salary":100000,"gender":"male"},
    102:{"name":"kumar","salary":75000,"gender":"male"}
}
print(employees)
print(employees[101]["name"])