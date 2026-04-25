# Read input from standard input
num = int(input())

# Check condition
if num > 0:
    print("Positive - check_number_sign.py:6")
elif num < 0:
    print("Negative - check_number_sign.py:8")
else:
    print("Zero - check_number_sign.py:10")

    #output:
    Enter a number: 5
    The number is Positive
    Enter a number: -3
    The number is Negative
    Enter a number: 0
    The number is Zero