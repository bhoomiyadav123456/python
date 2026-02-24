set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

if set1.issubset(set2):
    print("First set is subset of second set - check_subset.py:5")
else:
    print("First set is not subset of second set - check_subset.py:7")



    '''Output:'''
    Enter first set elements: 1 2
    Enter second set elements: 1 2 3 4
    First set is subset of second set