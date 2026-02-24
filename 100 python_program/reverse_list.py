# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list: - reverse_list.py:9", reversed_list)


'''Output:'''
Enter numbers separated by space: 1 2 3 4 5
Reversed list: [5, 4, 3, 2, 1]