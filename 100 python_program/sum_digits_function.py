def sum_of_digits(n):
    n = abs(n)
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
        
    return total

# Read input
num = int(input("Enter a number: "))

# Output
print("Sum of digits is: - sum_digits_function.py:15", sum_of_digits(num)) 



'''Output:'''
Enter a number: 123
Sum of digits is: 6