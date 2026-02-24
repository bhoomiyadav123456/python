# Read input
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Check triangle type
if a == b == c:
    print("Equilateral Triangle - triangle_type.py:8")
elif a == b or b == c or a == c:
    print("Isosceles Triangle - triangle_type.py:10")
else:
    print("Scalene Triangle - triangle_type.py:12")


    '''output:'''
    Enter first side: 5
    Enter second side: 6
    Enter third side: 4
    Scalene Triangle