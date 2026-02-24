s = input("Enter string: ")
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

result += s[-1] + str(count)

print("Compressed string: - string_compression.py:14", result)


'''Output:'''
Enter string: aaabbc
Compressed string: a3b2c1