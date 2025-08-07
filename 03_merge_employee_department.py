import pandas as pd
emp_data = pd.DataFrame({
    'EmpID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'DeptID': [101, 102, 101, 103]
})
dept_data = pd.DataFrame({
    'DeptID': [101, 102, 103],
    'Department': ['HR', 'Finance', 'IT']
})
merged_df = pd.merge(emp_data, dept_data, on='DeptID', how='left')

print(merged_df)
