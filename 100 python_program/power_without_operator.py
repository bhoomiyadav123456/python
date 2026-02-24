# Read input
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

for i in range(exp):
    result *= base

# Output
print("Result is: - power_without_operator.py:11", result)



'''Output:'''
Enter base: 2
Enter exponent: 3
Result is: 8