# Read input
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value: - max_in_tuple.py:10", maximum)



'''Output:'''
Enter numbers separated by space: 5 2 9 1 7
Maximum value: 9