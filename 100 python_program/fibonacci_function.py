def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series: - fibonacci_function.py:3")
    
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Read input
num = int(input("Enter number of terms: "))

# Output
fibonacci(num)



'''Output:'''
Enter number of terms: 6
Fibonacci series:
0 1 1 2 3 5 