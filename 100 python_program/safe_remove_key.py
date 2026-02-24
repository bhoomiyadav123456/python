d = eval(input("Enter dictionary: "))
k = input("Enter key to remove: ")

removed = d.pop(k, "Key not found")
print("Updated dictionary: - safe_remove_key.py:5", d)


'''Output:'''
Enter dictionary: {'a':1,'b':2}
Enter key to remove: a
Updated dictionary: {'b': 2}