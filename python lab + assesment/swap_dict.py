# Swap keys and values

data = {'a': 1, 'b': 2, 'c': 3}

swapped = {}

for key, value in data.items():
    swapped[value] = key

print(swapped)


'''Output'''
{1: 'a', 2: 'b', 3: 'c'}