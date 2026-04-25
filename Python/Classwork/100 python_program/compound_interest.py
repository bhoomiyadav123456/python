# Read input from standard input
principal = float(input())
rate = float(input())
time = float(input())

# Calculate Compound Interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

# Print the required output
print(compound_interest)

#output:
Enter principal amount: 1000
Enter rate of interest: 10
Enter time: 2
Compound Interest is: 210.0