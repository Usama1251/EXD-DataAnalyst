import pandas as pd

x = {
    'Name': ['Usama', 'Mobeen', 'Zia'],
    'Age': [1,2,3],
    'Country': ["PK", 'Ban', 'Ind'],
    'Dependent': ['Yes', 'No', 'No']
}

df = pd.DataFrame(x)

print(df)

