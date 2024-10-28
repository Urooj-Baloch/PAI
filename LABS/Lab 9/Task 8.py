import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y1 = [10, 15, 13, 20, 18, 25]  
y2 = [12, 17, 14, 19, 22, 24]  
plt.plot(x, y1, color='pink', marker='o', label='Y1 Data')

plt.plot(x, y2, color='gray', marker='o', label='Y2 Data')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(loc='lower right')

plt.show()