text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels: - count_vowels.py:10", count)

#output:
# Enter a string: Hello, World!
# Number of vowels: - count_vowels.py:10 3