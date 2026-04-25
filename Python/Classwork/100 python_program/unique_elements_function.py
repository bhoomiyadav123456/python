def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Output
print("Unique elements: - unique_elements_function.py:12", unique_elements(numbers))



'''Output:'''
Enter numbers separated by space:  1 2 2 3 4 4 5
Unique elements: [1, 2, 3, 4, 5]