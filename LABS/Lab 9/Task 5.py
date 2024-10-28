import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Name": ["Ali", "Zain", "Ayesha", "Fatima", "Omar", "Noor", "Khan", "Sara", "Hassan", "Meher"],
    "Age": [19, 25, 23, 24, 22, 27, 21, 20, 29, 18],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)

gender_counts = df['Gender'].value_counts()


plt.figure(figsize=(10, 10))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title("Gender Distribution Among Students")
plt.axis('equal')  
plt.show()
