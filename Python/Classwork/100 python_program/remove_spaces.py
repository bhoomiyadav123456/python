s = input("Enter string: ")
result = ""

for ch in s:
    if ch != " ":
        result += ch

print("Without spaces: - remove_spaces.py:8", result)


'''Output:'''
Enter string: hello world
Without spaces: helloworld