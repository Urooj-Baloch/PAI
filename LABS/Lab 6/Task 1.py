import pandas as pd
data = {
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Revenue': [2500000, 1500000, 3000000, 500000, 4500000],
    'Budget': [800000, 1200000, 600000, 300000, 900000]
}
df = pd.DataFrame(data)
filtered_movies = df[(df['Revenue'] > 2000000) & (df['Budget'] < 1000000)]
print("Movies with Revenue > 2 million and Budget < 1 million:")
print(filtered_movies if not filtered_movies.empty else "No movies found that meet the criteria.")
