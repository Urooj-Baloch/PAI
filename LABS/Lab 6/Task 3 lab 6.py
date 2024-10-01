import pandas as pd
student_data = {
    'name': ['Urooj', 'hania', 'Charlie', 'Adam', 'mahnoor', 'Fariha', 'noor', 'Hannah'],
    'age': [19, 22, 21, 23, 19, 20, 22, 21],
    'grade': [88, 92, 85, 90, 95, 87, 90, 88],
    'enrolled': ['yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no']
}
labels = ['1', '2', '3', '4', '5', '6', '7', '8']
df_students = pd.DataFrame(student_data, index=labels)
print("DataFrame from the specified dictionary:")
print(df_students)
