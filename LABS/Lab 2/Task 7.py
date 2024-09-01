temp = [23, 25, 21, 20, 30, 29, 27, 24, 26, 28, 22, 23, 24, 25,
                23, 21, 26, 27, 28, 29, 30, 24, 22, 20, 19, 25, 26, 27, 28, 29]
remove = int(input("Enter the day to remove: ")) -1
if 0 <= remove < len(temp):
    removed_temp = temp.pop(remove)
    print("Removed Temperature for Day ",remove +1,":",removed_temp,"°C")
else:
    print("Invalid day ")
    print("Temperatures after removal: ",temp)
    sorted_temp = sorted(temp)
    print("Sorted Temperatures: ",sorted_temp)
avg_temp = sum(temp) / len(temp)
print("Average Temperature: ",avg_temp,"°C")
H_temp = max(temp)
L_temp = min(temp)
print("Highest Temperature: ",H_temp,"°C")
print("Lowest Temperature: ",L_temp,"°C")



