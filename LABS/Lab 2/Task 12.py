l1 = input("Enter the first list of elements separated by spaces: ").split()
l2 = input("Enter the second list of elements separated by spaces: ").split()
if len(l1) != len(l2):
    print("Error: Both lists must have the same number of elements.")
else:
    dict = {}
    for i in range(len(l1)):
        key = l1[i]
        value = l2[i]
        dict[key] = value
    print("The resulting dictionary is:")
    print(dict)
