import pandas as pd
import matplotlib.pyplot as plt

sea_level_data = pd.read_csv('seaLevel.csv')


latest_year = sea_level_data['year'].max()
data_last_100_years = sea_level_data[sea_level_data['year'] >= latest_year - 100]

plt.figure(figsize=(12, 6))
plt.scatter(data_last_100_years['year'], data_last_100_years['mmfrom1993-2008average'], color='b', label='Sea Level (mm)')

plt.title("Sea Level Rise Over the Past 100 Years")
plt.xlabel("Year")
plt.ylabel("Sea Level Change from 1993-2008 Average (mm)")
plt.grid(True)
plt.legend()
plt.show()