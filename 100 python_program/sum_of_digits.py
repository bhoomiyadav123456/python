# Read input
num = int(input("Enter a number: "))

# Calculate sum of digits
sum_digits = 0
n = abs(num)

while n > 0:
    sum_digits += n % 10
    n = n // 10

print("Sum of digits is: - sum_of_digits.py:12", sum_digits)


#output:
Enter a number: 123
Sum of digits is: 6