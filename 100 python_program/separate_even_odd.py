# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers: - separate_even_odd.py:13", even)
print("Odd numbers: - separate_even_odd.py:14", odd)



'''Output:'''
Enter numbers separated by space: 1 2 3 4 5 6
Even numbers: [2, 4, 6]
Odd numbers: [1, 3, 5]