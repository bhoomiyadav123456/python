sentence = input("enter a sentence:")
#to count numbers of alphabets
count = 0
for x in sentence:
#to check x is alphabet or not
if x.isalpha():
    count = count + 1
print("Numbers of alphabets in sentence is: - ex_dict_2.py:8", count)

#output:
# enter a sentence:Hello, World! @2024
# Numbers of alphabets in sentence is: - ex_dict_2.py:8 10
