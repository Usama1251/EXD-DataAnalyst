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

#Del() used to delete the values from list

# list1 = [1,2,3,4,5,6,7,8]

# del list1[3:6]
# print(list1)

# Type casting used in list to convert string or any to list but char by char list  bnaye ga

# str1 = "Python is fun"
# print("og string ", str1)
# l1 = list(str1)
# print(l1)

# spilt() function used to convert string to list based on parameter

# str1 = "Python is fun"
# a = str1.split(" ")
# print(a)

# # #Join used to convert list to string

# list1 = ['a', 'b', 'c', 'd', 'e']
# a = " ".join(list1)
# print(a)

#Some builtin functions len(), max(), min(), sum()

# list_num = [1,2,3,4,51,6,7,8,9]

# print("Length of List = ", len(list_num))
# print("Max element in list = ", max(list_num))
# print("Min element in list = ", min(list_num))
# print("Sum of the elements in the list = ", sum(list_num))      

#In Aliasing, we used assignment opertor = to store same id value or point same address in memory 

# list1 = [1,2,3,4]
# list2 = list1
# list3 = [1,2,3,4]

# print("Id of old list = ", id(list1))
# print("Id of new list = ", id(list2))
# print("Id of 3rd list having same value as list 1 = ", id(list3))

# list2[2] = 9

# print("old list ", list1, id(list1))
# print("new list ", list2, id(list2))

#shallow copy creates a new list object in memory, refreneces will be different in memory, nested list ko copy nhi krta
 
# list1 = [1,2,3,4]
# list2 = list1[:]

# print("old list ", list1, id(list1))
# print("new list ", list2, id(list2))

#one more way to shallow copy is by import copy
# import copy

# list1 = [1,2,3,4]
# list2 = copy.copy(list1)
# list2[2] = 51
# print("old list ", list1, id(list1))
# print("new list ", list2, id(list2))

# list1 = [1,2,3,[4, 9], [5,7]]
# list2 = list1[:]
# list2[2] = 51
# print("old list ", list1, id(list1))
# print("new list ", list2, id(list2))
# print("\n")
# list2[3][0] = "a"
# print("old list ", list1, id(list1))
# print("new list ", list2, id(list2)) #so basically shallow copy nested ki value dono list me change kr deta mean outer list se kam krta not inner, but references will be different in outer but same in nested list

#use deep copy if nested list k values bhi change krni hogi both list se aur reference change hojaye ga nested me bhi
# import copy

# list1 = [[0,1], [2,3], [3,4]]
# list2 = copy.deepcopy(list1)

# list2[2][0] = "a"

# print("old list ", list1, id(list1))
# print("new list ", list2, id(list2))

#Sort functions used to sort the list

# list_num = [6, 5, 1, 9, 2]

# list_num.sort() #ascending number
# print(list_num)
# list_num.sort(reverse=True) #descending number
# print(list_num)

# list_alpha = ["c", "a", "z", "d"]

# list_alpha.sort()
# print(list_alpha)

# #Length ki base pr sort kre ga

# mul_List = ["dddd", "ccc", "aaaaaa", "bb"]
# mul_List.sort(key=len) 
# print(mul_List)

# list1 = ["abcz", "xyza", "bas", "kiran"]

# list1.sort(key= None, reverse=True) #last alphabet k base pr sorting
# print(list1)

# def last(word):
#     return word[-1]

# print(last('zainab'))

# list1 = ["abcz", "xyza", "bas", "kiran"]
# list1.sort(key=last)  #hr element k last alphabet se sorting krega
# print(list1)

# #membership operators

# list_num = [2,3,1,5,4]
# a = 5 in list_num
# print(a)