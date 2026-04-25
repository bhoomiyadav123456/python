s = input("Enter sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word: - longest_word.py:4", longest)


'''Output:'''
Enter sentence: I love programming
Longest word: programming