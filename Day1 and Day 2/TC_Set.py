myset={1,2,3,4,5,3,2,1}
print(myset)

#acessing set
for i in myset:
    print(i)

#set methods
myset.add(100)
print(myset)

#Union & Intersection
A={1,2,3}
B={3,4,5}
print(A|B) #Union
print(A&B) #Intersection

#Availability - Membership
print(2 in A)

#Assignment operator
a=b=c=2
print(b)