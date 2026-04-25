n = 5
for i in range(1, n+1):
    print("* - pattern_arrow.py:3"*i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*i)

    #output:
    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *
    