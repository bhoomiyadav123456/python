# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter value of K: "))

k = k % len(numbers)   # handle large K values

rotated = numbers[k:] + numbers[:k]

print("Rotated list: - rotate_list.py:9", rotated)


'''Output:'''
Enter numbers separated by space: 1 2 3 4 5
Enter value of K: 2
Rotated list: [3, 4, 5, 1, 2]