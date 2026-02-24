# Read input
num = int(input("Enter a number: "))

# Reverse the number
rev = 0
n = abs(num)

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

# If number is negative, keep sign
if num < 0:
    rev = -rev

# Print the required output
print("Reversed number is: - reverse_number.py:17", rev)


'''output:'''
Enter a number: 1234
Reversed number is: 4321