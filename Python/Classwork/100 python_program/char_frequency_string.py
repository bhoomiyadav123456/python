s = input("Enter string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for k in freq:
    print(k, ": - char_frequency_string.py:8", freq[k])


    '''Output:'''
    Enter string: hello
    h : 1
    e : 1
    l : 2
    o : 1