import matplotlib.pyplot as plt
import numpy as np
students = [
    "Ali", "Ayesha", "Omar", "Fatima", "Zain",
    "Hira", "Bilal", "Sara", "Kamran", "Nida",
    "Hassan", "Ibrahim", "Noor", "Sadia", "Mansoor",
    "Farah", "Sami", "Asma", "Rehan", "Maira"
]
heights = [160, 165, 170, 155, 180, 158, 172, 165, 177, 162,
           169, 174, 159, 168, 175, 182, 160, 164, 170, 155]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1) 
colors = plt.cm.viridis(np.linspace(0, 1, len(students)))  
plt.bar(students, heights, color=colors)
plt.title("Student Heights (Bar Chart)")
plt.xlabel("Students")
plt.ylabel("Height (cm)")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2) 
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Student Heights Distribution (Pie Chart)")

plt.tight_layout()
plt.show()
