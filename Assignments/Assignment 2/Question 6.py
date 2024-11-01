import numpy as np
arr=np.arange(4).reshape(2,2)
print(arr)
det=np.linalg.det(arr)
print("Determinant:\n",det)
inv=np.linalg.inv(arr)
print("Inverse:\n",inv)