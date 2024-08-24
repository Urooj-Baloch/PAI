l = []
list = int(input("Enter the size of the list: "))
n = int(input("Enter a number: "))

for i in range(0, list):
    element = int(input("Enter the elements of the list: "))
    if element >= n:
        l.append(element)

print("List after deleting elements smaller than", n, ":", l)
