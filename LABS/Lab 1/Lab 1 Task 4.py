l=[]
list=int(input(("Enter the size of list\n")))
sum=0
for i in range(0,list):
    element=int(input(("Enter the element of list\n")))
    sum=sum+element
    l.append(element)

print("Sum of given elements in list is:",sum)
