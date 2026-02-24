# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if numbers == numbers[::-1]:
    print("List is Palindrome - palindrome_list.py:5")
else:
    print("List is Not Palindrome - palindrome_list.py:7")



    '''Output:'''
    Enter numbers separated by space: 1 2 3 2 1
    List is Palindrome