# Flatten nested list

nested = [[1, 2], [3, 4], [5]]

flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)


'''Output'''
[1, 2, 3, 4, 5]