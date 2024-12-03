import pandas as pd
data = {
    "Patient_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Heart_Disease": ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No"],
    "Treatment": ["Medication", "Lifestyle Change", "Surgery", "None", "Medication", 
                  "Medication", "Lifestyle Change", "None", "Medication", "Lifestyle Change"],
}

df = pd.DataFrame(data)
print(df)

import pandas as pd

# Sample heart-related data
data2 = {
    "Patient_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [45, 60, 38, 50, 55, 65, 47, 55, 42, 51],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Cholesterol": [230, 250, 210, 260, 190, 270, 240, 230, 200, 210],
    "Blood_Pressure": [120, 130, 115, 140, 125, 135, 128, 142, 118, 130],
}

df2 = pd.DataFrame(data2)

# Display the DataFrame
print(df2)
result=pd.concat([df,df2],axis=1)
print(result)
sor=df2.sort_values("Age",inplace=False)
print(sor)
change=df2.at[0,"Age"]
print(change)
print(df2["Gender"])
sts=df2.describe()
print(sts)
df2['Cholesterol_Status'] = df2['Cholesterol'].apply(lambda x: 'High' if x > 240 else 'Normal')
print(df2)
df2.index=["First",'second','third','fourth','fifth','sixth','seventh','Eighth','ninth','tenth']
print(df2)