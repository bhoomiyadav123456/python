import numpy as np

arr = np.array([10, 25, 30, 5, 40])

indices = np.where(arr > 20)

print(indices)


'''Output'''
(array([1, 2, 4], dtype=np.int64),)