def count_vowels(s):
    vowels = "aeiou"
    count = 0
    
    for ch in s.lower():
        if ch in vowels:
            count += 1
            
    return count

# Read input
string = input("Enter a string: ")

# Output
print("Number of vowels: - count_vowels_function.py:15", count_vowels(string))



'''Output:'''
Enter a string: hello
Number of vowels: 2