#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
#List function in python
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
#count(x) - returns the number of times x appears in the list
#reverse(x) - reverses the order of the list
#create a list of 20 numbers given by user

numbers = []

#Take 20 numbers from user
print("Enter 20 numbers: - listfunction.py:11")
for i in range(20):
    num = int(input(" "))
    numbers.append(num)
    #display the list
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listfunction.py:16")
    print()
    remove_num = int(input("Enter a number to remove from the list: "))
    #_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    print("List is: - listfunction.py:20")
    print(numbers)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listfunction.py:22")
    #frequency of the number in the list
    frequency = numbers.count(remove_num)
    if(frequency==0):
        print(remove_num,"is not present in the list. - listfunction.py:26")
        elif(frequency==1):
print("As it is unique so,cannot be removed from list - listfunction.py:28")
else:
#to reverse the list
numbers.reverse()
for i in range(1,frequency):
    numbers.remove(remove_num)
numbers.reverse()
print("the list after removing: - listfunction.py:35",remove_num,"List"))
print(numbers)

#output:
# Enter 20 numbers: - listfunction.py:11
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# Enter a number to remove from the list: 5
# List is: - listfunction.py:20
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listfunction.py:22
# the list after removing: - listfunction.py:35 5 List
# [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
