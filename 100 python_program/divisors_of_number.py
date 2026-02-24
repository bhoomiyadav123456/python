# Read input
n = int(input("Enter a number: "))

print("Divisors are: - divisors_of_number.py:4")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


        '''Output:'''
        Enter a number: 12
        Divisors are:
        1 2 3 4 6 12