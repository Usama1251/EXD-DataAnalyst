# Reading file
# f = open('text.txt')
# print(f.read())

#also we can use with as it dont need to close file

# with open('text.txt') as f:
#     print(f.read())
    
# also readline()

# with open('text.txt') as f:
#     print(f.readline())
#     f.close()
 
# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'example1.txt'
# urllib.request.urlretrieve(url, filename)

# with open('example1.txt', 'r') as f:
#     print(f.read())

#Write mode in file  handling

# exmp2 = 'example2.txt'
# with open(exmp2, 'w') as writeFile:
#     writeFile.write("This is line A")
    
# with open('example2.txt', 'a') as appendFile:
#     appendFile.write("\nThis is line B")
    
# with open('example2.txt', 'r') as readFile:
#     with open('example3.txt', 'w') as writeFile:
#         writeFile.write(readFile.read())