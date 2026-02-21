n = 5
for i in range(n):
    for j in range(n):
        if i==j or i==0 or i==n-1 or j==0 or j==n-1:
            print("* - pattern_squarewithdiagonal.py:5", end="")
        else:
            print(" ", end="")
    print()

    #output:
    # *****
    # *   *
    # * * *
    # *   *
    # *****
    