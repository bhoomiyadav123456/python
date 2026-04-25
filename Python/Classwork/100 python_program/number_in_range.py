# Read input
num = int(input("Enter number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

# Check whether number lies in range
if lower <= num <= upper:
    print("Number is in range - number_in_range.py:8")
else:
    print("Number is not in range - number_in_range.py:10")


    '''Output:'''
    Enter number: 5
    Enter lower limit: 1
    Enter upper limit: 10
    Number is in range