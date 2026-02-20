#creating list of numbers
numbers = [45,47,89,34,56]

#display the list
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:5")
print("Numbers are: - listoperation.py:6", numbers)

#display data without square brackets
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:9")
print("Numbers are: - listoperation.py:10")
print(*numbers)

#display elements by using for loop
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:14")
print("Numbers are: - listoperation.py:15")
for num in numbers:
    print(num)


    length = len(numbers)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:21")
    print("Number of elements in list: - listoperation.py:22", length)

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:24")
    print("Numbers in reverse order: - listoperation.py:25")
    for index in range(length - 1, -1, -1):
        print(numbers[index],end=", - listoperation.py:27")

        #find sum of all numbers in list
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:30")
        sum = 0
        for i in numbers:
            sum=sum + i;
        print("Sum of all numbers in the list: - listoperation.py:34", sum)

        #finding greatest number in list
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:37")
        max=numbers[0]
        for index in range(1,length):
            if (max<numbers[index]):
                max=numbers[index]
                print("Maximum number in the list is: - listoperation.py:42", max)

                #ouput
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:5
                # Numbers are: - listoperation.py:6 [45, 47, 89, 34, 56]
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:9
                # Numbers are: - listoperation.py:10    45 47 89 34 56
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py:14
                # Numbers are: - listoperation.py:15    45
                # 47            
                # 89
                # 34
                # 56
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py
                # Number of elements in list: - listoperation.py:22 5
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py
                # Numbers in reverse order: - listoperation.py:25 56, - listoperation.py:27 34, - listoperation.py:27 89, - listoperation.py:27 47, - listoperation.py:27 45, - listoperation.py:27
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ -
                # Sum of all numbers in the list: - listoperation.py:34 271
                # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - listoperation.py
                # Maximum number in the list is: - listoperation.py:42 89   