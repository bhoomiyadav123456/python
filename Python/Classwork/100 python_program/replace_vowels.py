s = input("Enter string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print("Updated string: - replace_vowels.py:11", result)


'''Output:'''
Enter string: hello
Updated string: h*ll*