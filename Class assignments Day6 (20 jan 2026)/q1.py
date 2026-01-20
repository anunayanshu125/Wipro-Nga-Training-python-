#re.match()
import re
emp_id="EMP123"
result=re.match(r"^EMP\d{3}",emp_id)
if result:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")
#re.search()
text="admin@gmail.com"
email=re.search(r"[w\.-]+@[\w\.-]+\.\w+",text)
if email:
    print("Email Found")
else:
    print("Email Not Found")
#Meta-characters, special sequences
text1="Anunay_443 and Anshal"
pattern=r"\w+\d+"
match=re.search(pattern,text1)
if match:
    print("Matched Pattern:",match.group())
#Matched groups
match=re.search(r"([\w\.-]+)@([\w\.-]+)",text)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))