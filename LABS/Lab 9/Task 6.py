import matplotlib.pyplot as plt

students = ["Ali", "Ayesha", "Omar", "Fatima", "Zain",
            "Hira", "Bilal", "Sara", "Kamran", "Nida"]
math_marks = [85, 78, 92, 88, 95, 80, 72, 90, 83, 76]
science_marks = [89, 82, 94, 80, 90, 78, 70, 85, 88, 91]

plt.figure(figsize=(10, 6))
plt.scatter(math_marks, science_marks, color='orange', s=100, edgecolor='black', label="Students' Marks")

plt.title("Comparison of Marks in Mathematics and Science", fontsize=14)
plt.xlabel("Mathematics Marks", fontsize=12)
plt.ylabel("Science Marks", fontsize=12)

plt.legend(loc="upper left")

plt.grid(True)

plt.show()
