import numpy as np
arr=np.arange(20)
print("Array of 20:\n",arr)
resha=np.reshape(arr,(4,5))
print("Reshaped:\n",resha)
#we can do it in one step as well like arr=np.arange(20).reshape(4,5)