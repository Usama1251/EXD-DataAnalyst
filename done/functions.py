# def sums(a, b):
#     c = a+b
#     return c

# rv = sums(1,2)
# print(rv)

# def myLen(a):
    
#     """
#     This function used to count elements in a list and docstring must be first statement in function to display
#     """
#     count = 0
    
#     for i in a:
#         count = count + 1
#     return count

  
# myList = [1,2,3,4,5,7]
# b = myLen(myList)
# print(b)
# print(myLen.__doc__)

# def sums(a,b):
#     total = a+b
#     return total

# a = 10
# b = 10
# rv = sums(a,b)
# print(a, " + ", b, " = ", rv)

# def sumofSquares(l1):
#     rv = 0
#     for i in l1:
#         rv = rv + i*i
#     return rv

# list1 = [1,2,3]
# rv = sumofSquares(list1)

# print("Sum of square of list ", rv)

# def evenN(a):
#     list2 = []
#     for i in a:
#         if i % 2 == 0:
#             list2.append(i)
#     return list2
# list1 = [1,2,3,4,5,6,7,8,9]
# b = evenN(list1)
# print(b, type(b))

# list1 = [4,1,2,5,3]
# swap = 0

# for i in range(len(list1) - 1):
#     for j in range(len(list1) - 1 - i):
#         if list1[j] > list1[j + 1]:
#             swap = list1[j + 1]
#             list1[j + 1] = list1[j]
#             list1[j] = swap
#     print(list1)

# print("Final List ", list1)

# task1
# def div(a,b):
#     c = a/b
#     return c

# a = int(input("Enter first input "))
# b = int(input("Enter second input "))
# res = div(a,b)
# print(res)

# #task2 function we defined before be used to add two integers or strings?

# def sums(a,b):
#     c = a+b
#     return c

# a = int(input("Enter first input "))
# b = int(input("Enter second input "))
# res = sums(a,b)
# print(res)

# # task3 function we defined before be used to concatenate lists or tuples?

# def conc(a,b):
#     c = a + b
#     return c

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# con = conc(list1, list2)
# print(con)


# # Write a function code to find total count of word `little` in the given string: 

# def countMary(a):
#     c = a.count('little')
#     return c

# str = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
# str1 = str.lower()
# b = countMary(str1)
# print(b)

# pass by arguments of intrinsic types (immutable) they are passed by values

#Pass by value, such as list, tupples, sets, dictionary objects are passed as reference

# reference se actual list bhi sort hojaye gi if working on passed reference

# def simpleBot(message):
#     responses = {
#         "hi":"Hello there",
#         "how you doing": "I'm doing great, btw how's your day going? ",
#         "bye": "See ya"
#     }
#     a = message.lower()
#     return responses.get(message, "I dont understand")

# b = input("Enter anything ")
# c = simpleBot(b)
# print(c)

#variable arguments *args jitne zyada bhejne ho chle jaye ge, tupple treat hota hai
#**kwargs, dictionary treat hota hai
#passign arguments in real time
#import sys
#python functions.py 1 2 3 4 5
#sys.argv used to access arguments jo real time pr diyey

import sys

# def funcLen(a):
#     for i in a:
#         print(sys.argv[i], end= " ")


# funcLen(range(len(sys.argv)))

def sumCmd(a):
    sum = 0
    for i in a:
        sum = sum + int(sys.argv[i])
    print(sum)
sumCmd(range(1, len(sys.argv)))