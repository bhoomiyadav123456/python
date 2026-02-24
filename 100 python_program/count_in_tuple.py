# Read input
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))
element = int(input("Enter element to count: "))

count = 0

for num in numbers:
    if num == element:
        count += 1

print("Occurrence of - count_in_tuple.py:11", element, "is:", count)



'''Output:'''
Enter numbers separated by space: 1 2 2 3 2 4
Enter element to count: 2
Occurrence of 2 is: 3