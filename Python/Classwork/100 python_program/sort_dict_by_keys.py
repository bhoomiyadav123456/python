d = eval(input("Enter dictionary: "))

sorted_dict = dict(sorted(d.items()))

print("Sorted by keys: - sort_dict_by_keys.py:5", sorted_dict)


'''Output:'''
Enter dictionary: {'b':2, 'a':1, 'c':3}
Sorted by keys: {'a': 1, 'b': 2, 'c': 3}