# Read input
n = int(input("Enter a number: "))

# Calculate factorial using for loop
fact = 1

for i in range(1, n + 1):
    fact *= i

# Output
print("Factorial is: - factorial_for_loop.py:11", fact)



'''Output:'''
Enter a number: 5
Factorial is: 120