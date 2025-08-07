import pandas as pd

filter_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 28, 35, 22],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 55000, 58000, 49000]
}
filter_df = pd.DataFrame(filter_data)
filtered_df = filter_df[(filter_df['Age'] > 25) & (filter_df['Department'].isin(['HR', 'IT']))]
print(filtered_df)