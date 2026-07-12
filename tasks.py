import re

text = " H!e@l#l$o% t^h&e, W(o)r_l+d 123 ".lower().strip()
pattern = r"[^0-9a-z\s]" # ^ iska mtlb k digs space aur alphabets ko replace nhi krna baqi sb kr do

result = re.sub(pattern, "", text)
print(result)