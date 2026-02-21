n = 5
for i in range(1, n+1):
    print("* - pattern_butterfly.py:3"*i + " "*(2*(n-i)) + "*"*i)
for i in range(n, 0, -1):
    print("* - pattern_butterfly.py:5"*i + " "*(2*(n-i)) + "*"*i)

    #output:
    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *
        