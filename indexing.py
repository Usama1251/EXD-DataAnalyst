name = "Usama Mobeen"

#positive indexing
print(name[11])  # Output: k

#negative indexing
print(name[-6])  # Output: n

name[5] = "m"  # This will raise an error because strings are immutable in Python
print(name)  # Output: Usama Mobeen

str1 = "Hello, World!"
print(str1[7])  # Output: W