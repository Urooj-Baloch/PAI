import pandas as pd
sales_data = {
    'Harvest Year': [2020, 2021, 2022],
    'Region': ['North America', 'Europe', 'Asia'],
    'Fruit': ['Apples', 'Bananas', 'Cherries'],
    'Market Type': ['Organic', 'Conventional', 'Organic'],
    'Sales Volume (tons)': [1200, 1500, 800]
}
df_sales = pd.DataFrame(sales_data)
print("DataFrame Dimensions (Rows, Columns):", df_sales.shape)
print("Column Names:", df_sales.columns.tolist())
