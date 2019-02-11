x = int(input())
for m in range(0,x):
    n = int(input())
    sum = 0
    for i in range(1,n):

        if(n%i==0):
            sum=sum+i
    if sum==n:
        print("%d eh perfeito" % n)
    else:
        print("%d nao eh perfeito" % n)