n = 5   # you can change the value

for i in range(1, n + 1):
    # print spaces
    for j in range(n - i):
        print(" ", end=" ")
    
    # print *
    for k in range(i):
        print("* - pattern1.py:10", end=" ")
    
    print()

    #output

    #         *
    #       * *
    #     * * *
    #   * * * *
    # * * * * *
    