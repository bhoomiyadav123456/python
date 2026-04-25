dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print("Merged Dictionary: - merge_dictionaries.py:12", merged)



'''Output:'''
Enter first dictionary: {'a':1, 'b':2}
Enter second dictionary: {'c':3}
Merged Dictionary: {'a': 1, 'b': 2, 'c': 3}