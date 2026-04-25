def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Read input
num = int(input("Enter a number: "))

# Output
print("Factorial is: - factorial_function.py:11", factorial(num))


'''Output:'''
Enter a number: 5
Factorial is: 120