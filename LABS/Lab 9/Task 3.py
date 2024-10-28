import matplotlib.pyplot as plt
flavor_names = ["Mango Sorbet", "Chocolate Chip", "Berry Bliss", "Green Tea", 
                "Caramel Swirl", "Cookies and Cream", "Lemon", "Nutty Hazelnut", 
                "Banana", "Rocky Road Delight"]
scoops_sold = [130, 220, 95, 85, 175, 115, 60, 40, 75, 125]

plt.figure(figsize=(10, 10))
plt.pie(scoops_sold, labels=flavor_names, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
plt.title("Distribution of Ice Cream Sales by Flavor")

plt.axis('equal') 
plt.show()
