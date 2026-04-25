set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

result = set1 - set2

print("Difference (set1  set2): - set_difference.py:6", result)


'''Output:'''
Enter first set elements: 1 2 3
Enter second set elements: 2 4
Difference (set1 - set2): {1, 3}