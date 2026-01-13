#	Question – List, Dictionary & Set Comprehensions
#   Topic: Comprehensions in Python
#   Given a list:
data = [1, 2, 3, 4, 5, 6, 2, 4]
# 1. Create a list comprehension to store squares of all numbers
square_num_list=[x**2 for x in data]
print(square_num_list)

# 2. Create a set comprehension to store only unique even numbers
unique_even_num={x for x in data if x%2==0}
print(unique_even_num)

# 3. Create a dictionary comprehension where the key is the number and the value is its cube
cube_dict={x:x**3 for x in data}
print(cube_dict)