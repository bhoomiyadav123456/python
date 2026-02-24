# Read input
string = input("Enter a string: ").lower()

# Count vowels
vowels = "aeiou"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

# Output
print("Number of vowels: - count_vowels.py:13", count)


'''Output:'''
Enter a string: hello
Number of vowels: 2