a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result: - simple calculator.py:6", a + b)
elif op == "-":
    print("Result: - simple calculator.py:8", a - b)
elif op == "*":
    print("Result: - simple calculator.py:10", a * b)
elif op == "/":
    print("Result: - simple calculator.py:12", a / b)
else:
    print("Invalid operator - simple calculator.py:14")
