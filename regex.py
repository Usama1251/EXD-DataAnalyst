import re

# s1 = "Body is the main part of the text."
# pattern = r"Body"

# result = re.search(pattern, s1)

# if result:
#     print("Match found:", result.group())
# else:
#     print("No match found.")
    
# pattern = r"\d\d\d\d\d\d\d"
# text = "My phone number is 1234567"
# match = re.search(pattern, text)

# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")
    
# pattern = r'\W'
# text = "Hello, world!"
# matches = re.findall(pattern, text)
# print(matches) 

# pattern = r'st'
# text = "The Bodyguard is the best album of 'Whitney Houston'."
# matches = re.findall(pattern, text)
# print(matches)  

# split_array = re.split(r"\s", "This is a sample text to be split into words.")
# print(split_array)  



# subsitute method is used to replace a pattern in a string with a specified replacement string. It takes three arguments: the pattern to search for, the replacement string, and the input string. The method returns a new string with all occurrences of the pattern replaced by the replacement string.

# s2 = "The Bodyguard is the best album of 'Whitney Houston'."
# pattern = r"Whitney Houston"
# replacement = "Usama"

# result = re.sub(pattern, replacement, s2, flags = re.IGNORECASE)

# print(result)  # Output: The Bodyguard is the best album of 'Usama'.

# s3 = "House number- 1105"
# pattern = r'\d\d\d\d'

# result = re.search(pattern, s3)

# if result:
#     print("Match Found = ", result.group())
# else:
#     print("Not found")