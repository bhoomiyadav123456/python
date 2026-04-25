# Read input
num = int(input("Enter a number: "))

# Count digits
count = 0
n = abs(num)

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n = n // 10

# Output
print("Number of digits is: - count_digits.py:16", count)


'''Output:'''
Enter a number: 12345
Number of digits is: 5