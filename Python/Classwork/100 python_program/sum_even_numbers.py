# Read input
n = int(input("Enter value of N: "))

# Calculate sum of even numbers up to N
sum_even = 0
i = 2

while i <= n:
    sum_even += i
    i += 2

# Output
print("Sum of even numbers is: - sum_even_numbers.py:13", sum_even)


'''Output:'''
Enter value of N: 10
Sum of even numbers is: 30