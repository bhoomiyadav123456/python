# Check Armstrong number

n = 153

temp = n
digits = len(str(n))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp //= 10

print(sum_val == n)


'''Output'''
True