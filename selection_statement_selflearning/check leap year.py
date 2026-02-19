year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year - check leap year.py:4")
else:
    print("Not a Leap Year - check leap year.py:6")