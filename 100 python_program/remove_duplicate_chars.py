s = input("Enter string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates: - remove_duplicate_chars.py:8", result)



'''Output:'''
Enter string: programming
Without duplicates: progamin