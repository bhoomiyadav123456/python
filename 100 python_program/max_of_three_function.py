def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# Output
print("Maximum number is: - max_of_three_function.py:15", maximum(x, y, z))



'''Output:'''
Enter first number: 10
Enter second number: 25
Enter third number: 15
Maximum number is: 25