
# if (2 == 2 ):
#     print("True Statement")
#     print("K")
# else:
#     print("False Statement")
    
# emptyString = ""

# if emptyString:
#     print("True Statement")
#     print("K")
# else:
#     print("False Statement")
    
# print("This statement will always execute")

# x = int(input("Enter the number "))

# if (x%2 == 0):
#     print("Even number")
# else:
#     print("odd number")
    
# print("Bye")

# a = int(input("Enter a number"))
# b = int(input("Enter b number"))

# if (a>b):
#     print("a is greater than b. ")
#     print("I'm in if block")
# else:
#     print("a is smaller than b")
#     print("i'm neither in else block")
# print("I'm neither in if and else block")

# age = int(input("Enter your age "))

# if (age > 18):
#     print("You can enter")
# else: 
#     print("Go see meat load")
# print("Move on")

#python ternary operator

# age = int(input("Enter your age "))

# rv = 'adult' if age >= 18 else 'child'
# print(rv)

# num = int(input("Enter your number "))

# res = 'even' if (num%2==0) else 'odd'
# print(res)

#Nested if else

# age = int(input("Enter your age "))

# if (age>=18):
#     rv = input("Do you have National ID card ")
#     a = rv.lower()
#     if (a == 'y' or a == "yes"):
#         print("Welcome, you can vote")
#     else: 
#         print("Sorry you don't have CNIC, so you cannot vote")
# else:
#     print("You are too young to vote")

#Else if conditions

# x = int(input("Enter the marks "))

# if (x >= 90):
#     print("Grade A")

# elif (x >= 80 and x < 90):
#     print("Grade A-")

# elif (x >= 70 and x < 80):
#     print("Grade B+")

# elif (x >= 60 and x < 70):
#     print("Grade B-")

# elif (x >=50 and x < 60):
#     print("Grade C")

# elif (x >= 40 and x < 50):
#     print("Grade D")

# else:
#     print("Fail")
    
#pass 

# if (6 < 9):
#     pass
# print("code runs")

#Task 1
import calendar
#There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.

annieYear = 1996
janeYear = 1999

if (annieYear%4 == 0):
    print("Annie Birthday is Leap Year")
else:
    print("Annie Birthday is not Leap Year")

if (janeYear%4 == 0):
    print("Jane year is leap year")
else:
    print("Jane Birthday is not Leap Year")
    
print("\n")
#Task 2
##### 2. In a school canteen, children under the age of 9 are only given milk porridge for breakfast. Children from 10
# to 14 are given a sandwich, and children from 15 to 17 are given a burger. The canteen master asks the age of the 
# student and gives them breakfast accordingly. Sam's age is 10. Use if-else statement to determine what the canteen
# master will offer to him.

childrenAge = int(input("Enter Sam's Age "))

if (childrenAge <= 9):
    print("Only milk porridge for breakfast")
    
elif (childrenAge >= 10 and childrenAge <= 14):
    print("Only Sandwich")
    
elif(childrenAge >= 15 and childrenAge <=17):
    print("Only Burger")
    
else:
    print("Not valid age")