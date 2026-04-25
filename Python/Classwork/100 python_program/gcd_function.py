def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

# Read input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Output
print("GCD is: - gcd_function.py:12", gcd(x, y))



'''Output:'''
Enter first number: 24
Enter second number: 36
GCD is: 12