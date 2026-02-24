# Read input
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = list1 + list2
unique = []

for num in merged:
    if num not in unique:
        unique.append(num)

print("Merged list without duplicates: - merge_remove_duplicates.py:12", unique)



'''Output:'''
Enter first list: 1 2 3
Enter second list: 4 5 6
Merged list without duplicates: [1, 2, 3, 4, 5, 6]