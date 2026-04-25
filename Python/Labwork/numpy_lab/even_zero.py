import numpy as np
numbers = np.arange(1,11)
# replace even numbers with 0
numbers[numbers % 2 == 0] = 0
print(numbers)


'''output'''
[1 0 3 0 5 0 7 0 9 0]