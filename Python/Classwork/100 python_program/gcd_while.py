# Read input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find GCD using while loop (Euclidean algorithm)
a = abs(a)
b = abs(b)

while b != 0:
    a, b = b, a % b

# Output
print("GCD is: - gcd_while.py:13", a)
