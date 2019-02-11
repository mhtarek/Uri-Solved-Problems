while True:
    n = int(input())
    if n==0:
        break


    for i in range(n):
        for j in range(i,n+i):
            x = pow(2,j)
            xlen = len(str(abs(x)))

            if j==i:
                print("{:{r}d}".format(x, r=xlen),end='')
            else:
                print("{: {r}d}".format(x, r=xlen),end='')

        print()
    print()
