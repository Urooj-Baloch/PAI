import pandas as pd
df = pd.read_csv(r'C:\Users\student24\Desktop\excel\heart.csv')
df['sex'] = df['sex'].replace({1: 'Male', 0: 'Female'})

df.to_csv('updated_file.csv', index=False)

print("Conversion completed. Updated file saved as 'updated_file.csv'.")
