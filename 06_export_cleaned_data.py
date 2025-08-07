import pandas as pd
import numpy as np

df = pd.read_excel("HR_Raw_Data.xlsx")  
print("Original Data:")
print(df.head())

if 'Name' in df.columns:
    df['Name'].fillna("Unknown", inplace=True)
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].mean(), inplace=True)
if 'Salary' in df.columns:
    df['Salary'].fillna('0K', inplace=True)
    df['Salary'] = df['Salary'].astype(str).str.replace('K', '', regex=True).astype(int) * 1000
if 'Joining_Date' in df.columns:
    df['Joining_Date'] = pd.to_datetime(df['Joining_Date'].fillna('2000-01-01'))
if 'Joining_Date' in df.columns:
    df['Experience_Years'] = 2025 - df['Joining_Date'].dt.year
df.to_excel("Cleaned_HR_Data.xlsx", index=False)
df.to_csv("Cleaned_HR_Data.csv", index=False)

print("Cleaned data exported successfully!")
print(df.head())
