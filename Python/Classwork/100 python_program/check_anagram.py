s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagrams - check_anagram.py:5")
else:
    print("Not Anagrams - check_anagram.py:7")


    '''Output:'''
    Enter first string: listen
    Enter second string: silent
    Anagrams