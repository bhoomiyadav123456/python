def is_palindrome(s):
    return s == s[::-1]

# Read input
string = input("Enter a string: ")

# Output
if is_palindrome(string):
    print("Palindrome String - palindrome_string_function.py:9")
else:
    print("Not a Palindrome String - palindrome_string_function.py:11")


    '''Output:'''
    Enter a string: madam
    Palindrome String