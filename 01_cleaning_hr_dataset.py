import pandas as pd
import numpy as np  

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', None],
    'Age': [25, np.nan, 30, 35, 29, 40],
    'Salary': ['50K', '60K', None, '70K', '65K', '58K'],
    'Joining_Date': ['2020-01-10', '2019-07-23', None, '2018-05-20', '2021-03-15', '2022-11-11']
}
df = pd.DataFrame(data)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Name'].fillna("Unknown", inplace=True)
df['Salary'].fillna('0K', inplace=True)
df['Salary'] = df['Salary'].str.replace('K', '', regex=True).astype(int) * 1000
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'].fillna('2000-01-01'))
df['Experience_Years'] = 2025 - df['Joining_Date'].dt.year
print(df)
