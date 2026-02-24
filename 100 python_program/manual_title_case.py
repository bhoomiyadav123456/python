s = input("Enter sentence: ")
words = s.split()
title = ""

for w in words:
    title += w[0].upper() + w[1:].lower() + " "

print("Title case: - manual_title_case.py:8", title.strip())


'''Output:'''
Enter sentence: hello world
Title case: Hello World