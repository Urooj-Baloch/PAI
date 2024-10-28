import matplotlib.pyplot as plt
city_names = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Rawalpindi", 
              "Multan", "Hyderabad", "Peshawar", "Quetta", "Gujranwala"]
city_populations = [14910000, 11126285, 1015000, 3200000, 2113000, 
                    1500000, 1700000, 2000000, 1000000, 2000000]


plt.figure(figsize=(10, 6))
plt.barh(city_names, city_populations, color='lightcoral')
plt.xlabel("Population Count")
plt.ylabel("Cities List")
plt.title("Population Distribution in Major Pakistani Cities")
plt.show()
