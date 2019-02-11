while True:
    n = int(input())
    if n == 0:
        break
    layerN = int(n/2)
    if n%2==1:
        layerN+=1

    ar = [[1 for j in range(n)] for i in range(n)]
    a = 0;
    b = n-1
    for l in range(1,layerN+1):
        for i in range(a,b+1):
            for j in range(a,b+1):
                ar[i][j] = l
        a+=1
        b-=1

    for i in range(0,n):
        for j in range(0,n):
            if j==0:
                print("%3d" %ar[i][j],end='')
            else:
                print(" %3d" % ar[i][j],end='')
        print()
    print()