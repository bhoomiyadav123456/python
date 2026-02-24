# Read input
ch = input("Enter a character: ")

# Check whether character is digit or alphabet
if ch.isalpha():
    print("Alphabet - char_check.py:6")
elif ch.isdigit():
    print("Digit - char_check.py:8")
else:
    print("Neither alphabet nor digit - char_check.py:10")


    '''output:'''
    Enter a character: 5
    Digit
    Enter a character: h
    Alphabet