def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read input
num = int(input("Enter a number: "))

# Output
if is_prime(num):
    print("Prime Number - prime_check_function.py:15")
else:
    print("Not a Prime Number - prime_check_function.py:17")


    '''Output:'''
    Enter a number: 7
    Prime Number