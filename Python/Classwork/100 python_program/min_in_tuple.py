# Read input
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum value: - min_in_tuple.py:10", minimum)



'''Output:'''
Enter numbers separated by space: 5 2 9 1 7
Minimum value: 1