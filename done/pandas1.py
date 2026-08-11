import pandas as pd

# x = {
#     'Name': ['Usama', 'Mobeen', 'Zia'],
#     'Age': [1,2,3],
#     'Country': ["PK", 'Ban', 'Ind'],
#     'Dependent': ['Yes', 'No', 'No']
# }

# df = pd.DataFrame(x)

# print(df)

import pandas as pd

# pak_Weather = pd.DataFrame({
#     'city': ['Lahore', 'Karachi', 'Peshawar', 'Islamabad'],
#     'temperature': [45, 32, 12, 33]
# })

# uae_Weather = pd.DataFrame({
#     'city': ['Dubai', 'Sharja', 'Ajman', 'Abu Dhabi', 'Al Ain'],
#     'temperature': [41, 21, 22, 33, 45],
#     'humidity': [88, 33, 32, 11, 50]
# })

# df = pd.concat([pak_Weather, uae_Weather], axis=0, ignore_index=True) row wise

# df = pd.concat([pak_Weather, uae_Weather], axis=1, ignore_index=True)

# print(df)

# df = pd.read_csv(r"C:\Usama\Data Analyst\csvFile.csv")

# df['date'] = ['8/10/2026'] * 62

# print(df)

# pivot aur pivot table me difference

# pivot me duplicate entries nhi honi chaiyay
#then is case me pivot table use krna hai

data = pd.DataFrame({
    'gender': ['male', 'female', 'female', 'male', 'female'],
    'sport': ['cricket', 'cricket', 'basketball', 'basketball', 'cricket'],
    'age': [22,21,23,21,20],
    'height': [72,72,73,75,66],
    'weight': [200, 130, 150, 175, 170]   
})

pivot = pd.pivot_table(
    data,
    index='gender',
    columns='sport',
    values=['age', 'height', 'weight'],
    aggfunc='mean'
)

print(pivot)