import numpy as np
print("Even number matrix")
even_num_array = np.arange(20,38,2).reshape(3, 3)
print(even_num_array)
print("Multiply by 4:")
multiply_four=even_num_array*4
print(multiply_four)
print("Identity matrix 3X3:")
ide=np.identity(3)
print(ide)
print("Resultant matrix after multiply by identity matrix")
multiply=even_num_array*ide
print(multiply)