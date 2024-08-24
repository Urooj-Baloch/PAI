l=[]
largest=-1
list=int(input("Enter a list: "))
for i in range(list):
    element = int(input("Enter an element: "))
    if element>largest:
        largest=element
print('The largest element in list is',largest)