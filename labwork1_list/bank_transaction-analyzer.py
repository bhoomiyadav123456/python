transactions = [5000, -2000, 15000, -5000, 20000]

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

big_deposits = len([t for t in transactions if t > 10000])

print("Total Balance: - bank_transaction-analyzer.py:10", balance)
print("Largest Withdrawal: - bank_transaction-analyzer.py:11", largest_withdrawal)
print("Deposits > 10000: - bank_transaction-analyzer.py:12", big_deposits)

#output:
# Total Balance: - bank_transaction-analyzer.py:10 33000
# Largest Withdrawal: - bank_transaction-analyzer.py:11 -5000
# Deposits > 10000: - bank_transaction-analyzer.py:12 2
