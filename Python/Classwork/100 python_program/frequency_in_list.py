# Read input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements: - frequency_in_list.py:12")
for key in frequency:
    print(key, ": - frequency_in_list.py:14", frequency[key])


    '''Output:'''
    Enter numbers separated by space:  1 2 2 3 3 3
    Frequency of elements:
    1 : 1
    2 : 2
    3 : 3