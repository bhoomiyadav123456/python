#creating a list of 10 numbers with repeated numbers
numbers = [45,47,89,34,56,45,47,89,34,56]
#display the list
print("numbers are: - deletion in list.py:4")
print(numbers)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - deletion in list.py:6")
#to delete element at index 5
numbers.pop(5)
print("After deleting element at index 5: - deletion in list.py:9")
print(numbers)
numbers.pop()
print("after deleting last element: - deletion in list.py:12")
print(numbers)
#to delete 45
numbers.remove(45)
print("after deleting 45: - deletion in list.py:16")
print(numbers)
#to delete 45
numbers.remove(45)
print("after deleting 45: - deletion in list.py:20")
print(numbers)

#output:
# numbers are: - deletion in list.py:4
# [45, 47, 89, 34, 56, 45, 47, 89, 34, 56]
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ - deletion in list.py:6
# after deleting element at index 5: - deletion in list.py:9
# [45, 47, 89, 34, 56, 47, 89, 34, 56]
# after deleting last element: - deletion in list.py:12
# [45, 47, 89, 34, 56, 47, 89, 34]
# after deleting 45: - deletion in list.py:16   
# [47, 89, 34, 56, 47, 89, 34]
# after deleting 45: - deletion in list.py:20
# [47, 89, 34, 56, 47, 89, 34]
# Note: The last remove(45) does not change the list as there are no more 45s left in the list.