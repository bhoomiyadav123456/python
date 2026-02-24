text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency: - character_frequency.py:10")
for key in freq:
    print(key, ": - character_frequency.py:12", freq[key])



    '''Output:'''
    Enter a string: hello
    Character Frequency:
    h : 1
    e : 1
    l : 2
    o : 1