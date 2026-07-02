#q1
str1 = "Python is fun"
one = str1[::-1]
print("Question 1 = ", one)
#q2
two = "".join(str1.split()[::-1])
print("Question 2 = ", two)
#q3
three = str1.upper()
print("Question 3 = ", three)
#q4
four = str1.replace(" ", "")
print("Question 4 = ", four)
#q5
vowels = "aeiouAEIOU"
five = vowels.replace(vowels, "#")
print("Question 5 = ", five)
#q7
str2 = "lexicographically"
seven = max(str2)
print("Question 7 = ", seven)
#q8
x = input("Enter a string: ")
eight = "".join(sorted(x))
print("Question 8 = ", eight)
#q9
length1 = input("Enter your string to find last index? ")
nine = length1.rfind("") - 1
print("Question 9, The last of the index is: ", nine)

#q10
# space = " "
# y = space.join(['my', 'name', 'is', 'John'])
result = " ".join([str(one), str(two), str(three), str(four), str(five), str(seven), str(eight), str(nine)])
print(result)

pydor = "dad"

a = pydor[::-1]
b = pydor[::1]
print(a == b)
