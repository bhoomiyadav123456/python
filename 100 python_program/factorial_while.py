# Read input
n = int(input("Enter a number: "))

# Calculate factorial using while loop
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

# Output
print("Factorial is: - factorial_while.py:13", fact)


'''OUTPUT:'''
Enter a number: 8
Factorial is: 40320