# Read input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Find greatest number
if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d

# Output
print("The greatest number is: - greatest_of_four.py:18", greatest)



'''Output:'''
Enter first number: 9
Enter second number: 5
Enter third number: 4
Enter fourth number: 6
The greatest number is: 9