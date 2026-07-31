#While Loops

# number = 0

# while number < 7:
#     print(number)
#     number = number + 1
# print("Bye")

#Calculate factorial

# i = 1
# result = 1

# if i == 0:
#     result = 1
# else:
#     while(i<=5):
#         result = result*i
#         i+=1
#     print(result)

#Sum of numbers
# i = 0
# res = 0

# while (i <= 5):
#     res = res + i
#     i= i + 1
#     print(i, res)
# print("Sum ", res)

list1 = ['learning', 'is', 'fun', 'with', 'python']
# i = 0

# while (i<len(list1)):
#     print(list1[i])
#     i=i+1
# print("Bye")

# while (list1):
#     print(list1.pop())
# print("Outside")

# a = [1,2,3,4,5]
# i = 0

# while (a):
#     while(i < len(a)):
#         print("Inside loop ", a[i])
#         i+=1
#     print('outside loop ')
#     break #totally iteration khtm kr de ga even though its inner or outer
# print("Ends ")

n = 10
        
while (n > 0):
    n = n - 1
    if (n == 5 or n == 7):
        continue #used to skip current iteration aur agle pr chla jaye ga
    print(n)