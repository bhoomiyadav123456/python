import numpy as np
# create array from 1 to 25
numbers = np.arange(1,26)
# reshape into 5x5 matrix
matrix = numbers.reshape(5,5)
# extract middle 3x3 sub-matrix
middle_matrix = matrix[1:4,1:4]
print(middle_matrix)


'''output'''
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]