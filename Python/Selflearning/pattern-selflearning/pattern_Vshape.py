n = 5
for i in range(n):
    for j in range(2*n):
        if j==i or j==2*n-i-1:
            print("* - pattern_Vshape.py:5", end="")
        else:
            print(" ", end="")
    print()

    #output:
    # *       *
    #  *     *
    #   *   *
    #    * *
    #     *
    