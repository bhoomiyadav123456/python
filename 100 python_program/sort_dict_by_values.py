d = eval(input("Enter dictionary: "))

sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))

print("Sorted by values: - sort_dict_by_values.py:5", sorted_dict)


'''Output:'''
Enter dictionary: {'a':3, 'b':1, 'c':2}
Sorted by values: {'b': 1, 'c': 2, 'a': 3}