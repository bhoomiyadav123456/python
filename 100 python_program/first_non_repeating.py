s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First nonrepeating character: - first_non_repeating.py:5", ch)
        break


    '''Output:'''
    Enter string: swiss
    First non-repeating character: w