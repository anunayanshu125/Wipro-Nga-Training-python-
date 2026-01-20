import re
from re import search

text = "python is powerful"
result = re.match("python",text)
if result:
    print("match found")
else:
    print("match not found")

search_result = re.search("powerful",text)
print(search_result.group())
print(search_result.start())
print(search_result.end())

email = "admin@gmail.com"
if re.match(r"[a-zA-z]+@",email):
    print("valid Start")

result1=re.fullmatch(r"\d{10}","7458961278")
if result1:
    print("matched")
else:
    print("match not found")

print(re.findall(r"\d+","price 50 and 100"))

for n in re.finditer(r"\d+","A1, B33, C44"):
    print(n.group(),n.start(),n.end())



print(re.search(r"\d+","Age is 25" ))

print(re.search(r"^a.*c$","abnkugeudec"))

m = re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())

m1 = re.search(r"(?<=@)\w+","test@gmail.com")
print(m1.group())

n =re.search("python","Python",re.I)
print(n.group())


# Multilines
text4 = "one\ntwo\nthree\nthirty"
print(re.findall(r"^t\w+",text4,re.M))