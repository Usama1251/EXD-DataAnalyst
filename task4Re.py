# a = "1"
# b = "2"

# print(a + b)

# d = "ABCDEFG"
# print(d[0:3])  

# e = 'cloclrleclclt'

# print(e[::2])

# g = "Mary had a little lamb and, lamb wanna eat by snow"

# print(g.find('snow'))

# print(g.replace('Mary', 'bob'))

# print(g.replace(',', '.'))

# print(g.split(" "))
import re

str1 = "The quick brown fox jumps over the lazy dog."

pattern  = "Fox"
replacement = "Bear"

result = re.sub(pattern, replacement, str1, flags = re.IGNORECASE)
print(result)  

str2 = "how much wood would a woodchuck chuck if a woodchuck could chuck wood?"

pattern = r"woo"
print(re.findall(pattern, str2))




