a = "Thriller is the sixth studio album by American singer Michael Jackson. it was released on November 30, 1982, by Epic Records."
print(a.upper())
print(a.lower())
print(a.capitalize())
print(len(a))

#strip method

b = "  i have done i strip  helo   "
print(b.strip()) #removes white spaces from both sides
print(b.lstrip()) #removes white spaces from left side
print(b.rstrip()) #removes white spaces from right side

#split method

c = "Learning Python is fun"
print(c.split()) #splits the string into a list of words based on the argument passed to the split method. By default, it splits on whitespace.

print(c.split("i")) #splits the string into a list of words based on the argument passed to the split method. By default, it splits on whitespace.

