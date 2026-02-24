# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for num in numbers:
    total += num

print("Sum of elements: - sum_of_list.py:8", total)


'''Output:'''
Enter numbers separated by space: 1 2 3 4 5
Sum of elements: 15