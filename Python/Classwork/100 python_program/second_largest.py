# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest number is: - second_largest.py:13", second)



'''Output:'''
Enter numbers separated by space: 10 25 40 15 30
Second largest number is: 30