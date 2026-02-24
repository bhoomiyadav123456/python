# Read input
num = int(input("Enter a number: "))

# Check Armstrong number
n = abs(num)
digits = len(str(n))
temp = n
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** digits
    temp = temp // 10

# Output
if armstrong_sum == n:
    print("Armstrong Number - armstrong_number.py:17")
else:
    print("Not an Armstrong Number - armstrong_number.py:19")



    '''Output:'''
    Enter a number: 153
    Armstrong Number