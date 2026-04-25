# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates: - remove_duplicates.py:10", unique)


'''Output:'''
 Enter numbers separated by space:  1 2 2 3 4 4 5
List after removing duplicates: [1, 2, 3, 4, 5]