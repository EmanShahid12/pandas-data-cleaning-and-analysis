import pandas as pd
sales_data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'Sales': [1000, 1500, 2000, 2500, 3000, 3500]
}
sales_df = pd.DataFrame(sales_data)
product_group = sales_df.groupby('Product')['Sales'].sum()
region_product_group = sales_df.groupby(['Region', 'Product'])['Sales'].sum()
print("Product-wise Total Sales:", product_group)
print("Region and Product-wise Sales:", region_product_group,)

