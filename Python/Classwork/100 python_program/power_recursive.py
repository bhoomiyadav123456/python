def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Read input
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

# Output
print("Result is: - power_recursive.py:11", power(b, e))



'''Output:'''
Enter base: 2
Enter exponent: 4
Result is: 16