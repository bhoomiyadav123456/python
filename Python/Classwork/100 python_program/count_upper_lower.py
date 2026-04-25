s = input("Enter string: ")
upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase: - count_upper_lower.py:10", upper)
print("Lowercase: - count_upper_lower.py:11", lower)


'''Output:'''
Enter string: HelloWorld
Uppercase: 2
Lowercase: 8