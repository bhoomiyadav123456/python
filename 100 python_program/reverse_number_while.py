# Read input
num = int(input("Enter a number: "))

# Reverse number using while loop
rev = 0
n = abs(num)

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

# Preserve negative sign if number is negative
if num < 0:
    rev = -rev

# Output
print("Reversed number is: - reverse_number_while.py:17", rev)


'''Output:'''
Enter a number: 1234
Reversed number is: 4321