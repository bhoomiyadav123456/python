set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

result = set1 ^ set2

print("Symmetric Difference: - symmetric_difference.py:6", result)



'''Output:'''
Enter first set elements: 1 2 3
Enter second set elements: 3 4 5
Symmetric Difference: {1, 2, 4, 5}