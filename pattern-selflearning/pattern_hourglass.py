n = 5
# Upper part
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
# Lower part
for i in range(2, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

    #output:
    # *********
    #  *******
    #   *****
    #    ***
    #     *
    #     *
    #    ***
    #   *****
    #  *******
    # *********

        