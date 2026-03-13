import numpy as np
# create random 5x5 matrix
matrix = np.random.randint(1,101,(5,5))
# find minimum and maximum
minimum_value = np.min(matrix)
maximum_value = np.max(matrix)
print("Matrix:\n - matrix_minmax.py:7", matrix)
print("Min = - matrix_minmax.py:8", minimum_value)
print("Max = - matrix_minmax.py:9", maximum_value)