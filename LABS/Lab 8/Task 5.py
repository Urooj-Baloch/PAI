import numpy as np
print("Random matrix:")
choices = [2, 5, 9, 10]
random_matrix = np.random.choice(choices, size=(4, 4))
print(random_matrix)
print("Identity matrix:")
ide=np.identity(4)
print(ide)
print("Multiply random matrix to identity matrix:")
multiply=random_matrix*ide
print(multiply)
print("Odd matrix:")
odd_numbers = np.arange(1, 32, 2).reshape(4, 4)
print(odd_numbers)
print("Addition of odd number matrix and multiply")
added_matrices=multiply+odd_numbers
print(added_matrices)
