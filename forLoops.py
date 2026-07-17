#iterable or iterator

#Loops

# list1 = ['kiran', 'khursheed', 'aqsa', 'sana', 'wajeeha', 'basirat', 'hrm']

# for i in list1:
#     print(i)

# print("Bye") 

# dict1 = {
#     "id": [1,2,3,4,5],
#     "name": ["usama", "mobeen", "zia", "awais", "ali"]
# }

# for i in dict1.values():
#     print(i)

#using range

# rv = range(-5, 2, 1)

# print(list(rv))

# x = int(input("Enter a number "))

# tables = (range(1, 11))
# mult = 1

# for i in tables:
#     mult = x * i
#     print(f"{x} * {i} = {mult}")

#enumerate gives u index as well as value

# name = ["usama", "mobeen", "zia", "awais", "ali"]

# for i, name in enumerate(name):
#     print(f"Value {name} is at {i}")

palindList = ['bob', 'dad', 'mom', 'cherry']
list1 = ["usama", "mobeen", "zia", "awais", "ali"]

newList = [i for i in palindList if (i == i[::-1])] #ik line me coding krna is comprehension

print("only palindrome ", newList)

newList = [i[::-1] for i in list1]
print(newList)




