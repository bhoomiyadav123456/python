# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Bubble Sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list: - sort_without_sort.py:10", numbers)


'''Output:'''
Enter numbers separated by space: 5 2 9 1 3
Sorted list: [1, 2, 3, 5, 9]