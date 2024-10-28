import matplotlib.pyplot as plt

student_ages = [19, 21, 23, 26, 28, 30, 32, 34, 36, 22, 25, 29, 33, 37, 24, 27, 35, 38, 40, 21, 22, 31]

age_distribution = {"18-24": 0, "25-29": 0, "30-34": 0, "35-39": 0, "40 and above": 0}
for age in student_ages:
    if 18 <= age <= 24:
        age_distribution["18-24"] += 1
    elif 25 <= age <= 29:
        age_distribution["25-29"] += 1
    elif 30 <= age <= 34:
        age_distribution["30-34"] += 1
    elif 35 <= age <= 39:
        age_distribution["35-39"] += 1
    else:
        age_distribution["40 and above"] += 1
labels = age_distribution.keys()
sizes = age_distribution.values()

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Distribution of Students by Age Group")

plt.axis('equal')
plt.show()
