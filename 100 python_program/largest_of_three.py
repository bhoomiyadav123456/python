# Read input from standard input
a = int(input())
b = int(input())
c = int(input())

# Find the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Print the required output
print(largest)

#output:
