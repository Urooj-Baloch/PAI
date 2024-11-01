import numpy as np
A = np.array([[1, 1, 0],[0, 1, 0],[0, 0, 1]])
b = np.array([1, 3, 2])
solution = np.linalg.solve(A, b)
print("Solution for x,y,z:", solution)
