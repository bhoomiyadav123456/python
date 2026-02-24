# Read input
numbers = tuple(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == len(set(numbers)):
    print("All elements are unique - unique_tuple.py:5")
else:
    print("Elements are not unique - unique_tuple.py:7")



    '''Output:'''
    Enter numbers separated by space: 1 2 3 4
    All elements are unique