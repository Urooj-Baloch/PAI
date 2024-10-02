import pandas as pd
df = pd.read_csv(r'C:\Users\student24\Desktop\excel\heart.csv')

filtered_df = df[df['ca'] == 2]

print(filtered_df)
