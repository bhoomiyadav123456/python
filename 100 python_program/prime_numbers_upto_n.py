# Read input
n = int(input("Enter value of N: "))

print("Prime numbers are: - prime_numbers_upto_n.py:4")

# Check numbers from 2 to N
for num in range(2, n + 1):
    is_prime = True
    
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    else:
        is_prime = False

    if is_prime:
        print(num, end=" ")


        '''Output:'''
        Enter value of N: 20
        Prime numbers are:
        2 3 5 7 11 13 17 19 