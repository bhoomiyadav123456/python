# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print("Average of elements: - average_of_list.py:10", average)



'''Output:'''
Enter numbers separated by space: 10 20 30 40
Average of elements: 25.0