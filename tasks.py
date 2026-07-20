#Print numbers from 1 to 20 using a for loop.

# a = range(20)

# for i in a:
#     print(i)
# Print numbers from 20 to 1 using a while loop.
# a = 20

# while (a >= 1):
#     print(a)
#     a -= 1

# Print only even numbers from 1 to 50.

# a = range(51)

# for i in a:
#     if i % 2==0:
#         print(i)
# Print only odd numbers from 1 to 50.

# for i in a:
#     if i % 2 != 0:
#         print(i)

# Print the multiplication table of a number entered by the user.

# a = int(input("enter a number "))
# b = range(11)

# for i in b:
#     print(a, "*", i, a*i) 

# Find the sum of numbers from 1 to 100.

# a = range(101)
# res = 0

# for i in a:
#     res +=i
# print(res)

# Find the factorial of a number.

# a = 3
# fac=1

# while (a >= 1):
#     fac *= a
#     a-=1
# print("factorial ", fac)

# Count how many numbers are divisible by 3 between 1 and 100.

# a = range(7)
# b = 0
# for i in a:
#     if (i%3 == 0):
#         b+=1
# print(b)   

# *
# **
# ***
# ****
# *****

# for i in range(6):
#     for j in range(i):
#         print("*", end="")
#     print()

# *****
# ****
# ***
# **
# *
# a = 0

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#         j-=1
#     print()

# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()