keys = input("Enter keys: ").split()
values = list(map(int, input("Enter values: ").split()))

d = dict(zip(keys, values))
print("Dictionary: - dict_from_lists.py:5", d)


'''Output:'''
Enter keys: a b c
Enter values: 1 2 3
Dictionary: {'a': 1, 'b': 2, 'c': 3}