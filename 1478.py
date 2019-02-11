while True:
    n = int(input())
    if n==0:
        break

    ar = [[1 for j in range(n)] for i in range(n)]

    a = 0
    for i in range(n):
        for j in range(n):
            x=abs(i-j)+1
            if j==0:
                print("%3d" % x, end='')
            else:
                print(" %3d" %x,end='')
        print()
    print()