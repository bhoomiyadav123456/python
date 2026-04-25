import numpy as np
random_array = np.random.rand(10)
normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))

print("Original Array: - normalize_array.py:5",random_array)
print("Normalized Array: - normalize_array.py:6",normalized_array)


'''output'''
Original Array: [0.54 0.21 0.87 0.12 0.63 0.45 0.78 0.33 0.56 0.91]

Normalized Array: [0.56 0.12 0.95 0.00 0.67 0.44 0.84 0.28 0.59 1.00]