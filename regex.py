import re

# s1 = "Body is the main part of the text."
# pattern = r"Body"

# result = re.search(pattern, s1)

# if result:
#     print("Match found:", result.group())
# else:
#     print("No match found.")
    
pattern = r"\d\d\d\d\d\d\d"
text = "My phone number is 1234567"
match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
    