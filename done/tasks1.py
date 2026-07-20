# import re

# text = " H!e@l#l$o% t^h&e, W(o)r_l+d 123 ".lower().strip()
# # pattern = r"[^0-9a-z\s]" # ^ iska mtlb k digs space aur alphabets ko replace nhi krna baqi sb kr do

# # result = re.sub(pattern, "", text)
# # print(result)


# pattern = r'[^0-9A-Za-z\s]'
# result = re.sub(pattern, "", text)
# print(result)

roman = input("Enter Roman Number (I to XXX): ").upper()

total = 0

values = {
    "I": 1,
    "V": 5,
    "X": 10
}

for i in range(len(roman)):
    if i < len(roman) - 1 and values[roman[i]] < values[roman[i + 1]]:
        total -= values[roman[i]]
    else:
        total += values[roman[i]]

print("Integer =", total)