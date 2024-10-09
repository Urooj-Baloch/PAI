import numpy as np
print("Array 1:")
arr=np.arange(20,50,2).reshape(5,3)
print(arr)
print("Array 2:")
arr2=np.arange(12,30,3).reshape(3,2)
print(arr2)
print("Resultant matrix:")
#the simple multiplication cant be applied because of multiplication rule of matrices so we use dot function
resultant=np.dot(arr,arr2)
print(resultant)