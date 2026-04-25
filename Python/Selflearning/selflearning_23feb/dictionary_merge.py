dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5}

# Merge dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)

print("First Dictionary: - dictionary_merge.py:8", dict1)
print("Second Dictionary: - dictionary_merge.py:9", dict2)
print("Merged Dictionary: - dictionary_merge.py:10", merged_dict)

#output:
# First Dictionary: - dictionary_merge.py:8 {'a': 1, 'b': 2, 'c': 3}
# Second Dictionary: - dictionary_merge.py:9 {'d': 4, 'e': 5}
# Merged Dictionary: - dictionary_merge.py:10 {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}