import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "John", "Ayesha"],
    "Age": [22, 21, 23, 24, 20],
    "Marks": [85, 92, 78, 90, 88],
    "Country": ["Pakistan", "USA", "Pakistan", "Canada", "Pakistan"]
}

s = pd.DataFrame(data)

s.insert(2, "Gender", [ "Male", "Female", "Male", "Male", "Female"])
# s.drop("Marks", axis=1, inplace=True)
# s.drop(['Gender', "Country"], axis=1,inplace=True)
# del s['Gender']
# s.pop("Gender")

# s.rename(
#     columns={
#         "Marks": "Score",
#         "Country": "City"
#     },
#     inplace=True
# )

s.loc[s['Marks'] >= 90, 'Grade'] = 'A'

s.loc[s['Marks'] <=89, 'Grade'] = 'B'

s.loc[s['Marks'] <=79, 'Grade'] = 'C'

print(s)

# s['City'] = ["Lahore", 'Karachi', "Islamabad", "Toronto", "Karachi"]
# s['Pass'] = s['Marks'] >= 80
# s['Marks'] = s['Marks'] + 5
# print(s)

# print(s.sort_values(["Age", "Marks"], ascending = [True, False]))
# print(s.sort_index(ascending=False))
#to save changes use inpace = true

# print(s.sort_values(['Marks']).reset_index(drop=True))

# Sort students by Age (ascending).
# print(s.sort_values("Age"))
# Sort students by Marks (descending).
# print(s.sort_values("Marks", ascending=False))

# Country (A–Z)
# Marks (High → Low)

# print(s.sort_values(['Country', 'Marks'], ascending = [True, False]))

# Sort by Name alphabetically.
# print(s.sort_values("Name"))

# Sort by Marks, then reset the index.


# print(s.sort_values("Marks").reset_index(drop=True))

# print(s['Name'].notna())
# print(s["Age"].between(21, 23))

# print(s['Age'])

# print(s[['Name', 'Country']])

# Using .loc, print the complete row with index 2.

# print(s.loc[2, ['Name', 'Age']])

# Using .loc, print the Marks of Sara.

# print(s.loc[1, "Marks"])
# Using .iloc, print the value in the 3rd row and 2nd column.

# print(s.iloc[2, 1])

# Using .iloc, print only the first two rows and first three columns.

# print(s.iloc[0:2, 0:3])