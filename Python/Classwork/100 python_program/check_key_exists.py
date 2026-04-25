d = eval(input("Enter dictionary: "))
key = input("Enter key to check: ")

if key in d:
    print("Key exists - check_key_exists.py:5")
else:
    print("Key does not exist - check_key_exists.py:7")


    '''Output:'''
    Enter dictionary: {'x':1,'y':2}
    Enter key to check: x
    Key exists