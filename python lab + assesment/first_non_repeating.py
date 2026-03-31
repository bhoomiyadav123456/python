# First non-repeating character

text = "aabbcde"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:
    if freq[ch] == 1:
        print("First nonrepeating character: - first_non_repeating.py:12", ch)
        break

    '''output'''
    First nonrepeating character: c
    