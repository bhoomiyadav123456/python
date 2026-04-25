# Read input
year = int(input("Enter a year: "))

# Check leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year - leap_year.py:6")
else:
    print("Not a Leap Year - leap_year.py:8")
    

    '''output:'''
    Enter a year: 2023
    Not a Leap Year