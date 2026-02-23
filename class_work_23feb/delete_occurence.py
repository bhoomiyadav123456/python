# Create a list of 20 numbers
numbers = [10, 5, 7, 5, 3, 9, 5, 2, 8, 6, 5, 1, 4, 5, 11, 12, 5, 13, 14, 5]

print("Original List: - delete_occurence.py:4")
print(numbers)

# Ask user to input a number
num = int(input("Enter a number to delete (except first occurrence): "))

# Check if number exists in list
if num in numbers:
    first_index = numbers.index(num)  
    
    new_list = []
    count = 0
    
    for i in numbers:
        if i == num:
            count += 1
            if count == 1:
                new_list.append(i)
        else:
            new_list.append(i)
    
    numbers = new_list
    print("Updated List: - delete_occurence.py:26")
    print(numbers)
else:
    print("Number not found in the list. - delete_occurence.py:29")

    #output:
# Original List: - delete_occurence.py:4
# [10, 5, 7, 5, 3, 9, 5, 2, 8, 6, 5, 1, 4, 5, 11, 12, 5, 13, 14, 5]
# Enter a number to delete (except first occurrence): 5 
# Updated List: - delete_occurence.py:26
# [10, 5, 7, 3, 9, 2, 8, 6, 1, 4, 11, 12, 13, 14]
