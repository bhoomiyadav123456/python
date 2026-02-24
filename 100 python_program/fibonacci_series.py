# Read input
n = int(input("Enter number of terms: "))

# Generate Fibonacci series using while loop
a = 0
b = 1
i = 1

print("Fibonacci series: - fibonacci_series.py:9")

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1


    '''Output:'''
    Enter number of terms: 8
    Fibonacci series:
    0 1 1 2 3 5 8 13