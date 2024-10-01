import pandas as pd

df = pd.read_csv('alcohol_consumption.csv')

filtered_df = df[(df['Year'] == 1987) | (df['Year'] == 1989)]

print(filtered_df)