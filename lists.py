# #List

# # empty
# list1 = []
# print(list1)

# #int
# list2 = [1,2,3,4]
# print(list2)

# #float
# list3 = [1.2, 2.3, 4.5, 6.8]
# print(list3)

# #string
# list4 = ["Usama", "Mobeen", "Zia"]
# print(list4)

# #bool
# list5 = [True, False, True]
# print(list5)

# #Nested List
# #Hetrogenous List diff data types

# list6 = [1, 2, 3, ["Usama", "Mobeen", 2], [1.2, 2.3, 3.4]]
# print(list6)

# x = [1,2,3]
# y = [1,2,3]

# print(id(x), id(y), x is y, x == y)

#x is y false is liyey k memory address are different for both of these variables, value = true hogi lkin id dono ki different hogi becoz list k case me mutable hai

#Lists are mutable and address will be same as lists are mutable to memory me same list pr value replace kr de ga existing list me

# numbers = [10,20,30,40,50,60]
# print(id(numbers))
# numbers[0] = 55

# print(numbers, id(numbers))

#Lists can have duplciate values

# list1 = ['Usama', 'Usama', 'Mobeen', 'Zia', 'Mobeen']
# print(list1)

# list2 = ["Usama", 1, 2.5, [10, "Mobeen"]]

# print(list2[0][1:2]) #indexing
# print(list2[3][1]) #accessing nested loops
# print(list2[3])
# print(list2[3][1][0:1]) #indexing in nested list

#Negative indexing

# L = ["Michael Jackson", 10.1, 1982]
# print(L)
# print("Last Index can access with negative index 1", L[-1], "\nLast Index can access with negative index 2", L[-2], "\nLast Index can access with negative index 3", L[-3])

#accessing list using slicing
# L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
# print(L[3:5])

# List Concatenatng 

# a = [1,2,3]
# b = [4,5]
# b = a + b
# print(b)

# c = [0] + b
# print(c)

# food_items1 = ["apple", "mango", "grapes"]
# food_items2 = ["meat", "spices", "burger"]

# food = food_items1 + food_items2
# print(food*3)
# print(food[1::2])

#replacing multuple element using slicing

# mylist = ['Data Science', 'Machine Learning', 2, 5, 7.0]

# mylist[0:2] = ['English', 'Urdu']
# mylist[0] = ['English', 'Urdu'] #nested wla concept
# print(mylist)

#for single element needs to add at the end of list use append() and returns none, void, use actual list not assignment var

# list1 = [1,2,3,4,5]

# list1.append(22)
# print(list1)

# a = list1.append(22)
# print(a) #returns none but it will append the 22 value to the list but can't assign list to  new var as it returns none

#adds single value at the end

# list1.append([4.61, "Usama"]) #makes and adds nested list into existing list
# print(list1)

#Extend() takes list of items and insert into existing list without making any nested list returns none
#adds multiple value at the end

# list1 = [1,2,3,4,5]

# list1.extend(["Waleed", 2.1]) 
# print(list1)

# list2 = ["Fruits", "Apple", "items"]
# list3 = ["Fruits", "Apple", "items"]
# list2.extend(list3)
# print(list2)

#Insert() used when ik specific position pr add krna ho and returns none

# myFamily = ["Usama", "Mobeen", "Zia"]
# print("Original Family List ", myFamily)

# myFamily.insert(1, "Hi")
# print(myFamily)

#Remove()
#using pop removes last index value if no argument is passed from the list and returns value

# list1 = ["Learning", "Is", "Fun", "with", "Python"]
# print("Original list", list1)
# a = list1.pop(0)
# b = list1.pop(-1)
# print("Pos After removed list ", list1, "Removed Item: ", a)
# print("Neg After removed list ", list1, "Removed Item: ", b)

#using remove() used when wanna remove with the value not by index and if same multiple values are in list then it will remove the first occurence 
#returns none

# list1 = ["Learning", "Is", "Fun", "with", "Python", "Is"]
# a = list1.remove("Is")
# print(list1)
# print(a) #returns none

#using clear() used to clear all elements in the list and returns none

# list1 = ["Learning", "Is", "Fun", "with", "Python"]
# a = list1.clear()
# print(list1)
# print(a)
