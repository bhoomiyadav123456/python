n = 5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("* - pattern_X.py:5", end="")
        else:
            print(" ", end="")
    print()

    #output:
    # *   *
    #  * *
    #   *
    #  * *
    # *   *
        
    