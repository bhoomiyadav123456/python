import numpy as np

arr = np.array([10, 20, 30, 40, 50])

norm = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print(norm)


'''Output'''
[0.   0.25 0.5  0.75 1.  ]