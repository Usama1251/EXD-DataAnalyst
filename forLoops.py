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

#reverse nikal k de ga using comprehension
newList = [i[::-1] for i in list1]
print(newList)

#palindrom nikal k de ga using comprehension
newList = [i for i in palindList if (i == i[::-1])] #ik line me coding krna is comprehension

print("only palindrome ", newList)

list2 = [1,2,3,4,5]

dict1 = {
    key: key**3 for key in list2
}
print("Dictionary ", dict1)

list3 = range(11)
dict2 = {
    key: key**3 for key in list3 if key**3%4 == 0
}
print(dict2)

dict3 = {
    'milk': 123.0,
    "chocolate": 21,
    'bread': 90
}

newDict = {
    key: value * 1.25 for key, value in dict3.items()
}

print("Raised prices by 25%", newDict)

