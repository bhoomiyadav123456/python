# Initialize sum
total = 0

print("Enter numbers (enter 0 to stop): - sum_until_zero.py:4")

while True:
    num = int(input())
    if num == 0:
        break
    total += num

# Output
print("Sum is: - sum_until_zero.py:13", total)



'''Output:'''
Enter numbers (enter 0 to stop):
5
3
2
0
Sum is: 10