x = int(input())
for j in range(0,x):
    flag = 0
    n = int(input())

    if n==1 or n==2:
        print("%d eh primo" %n)
    elif n>2:
        for i in range(2,n):
            if n%i==0:
                flag = 2
                break
            else:
                flag = 1

    if(flag==1):
        print("%d eh primo" % n)
    elif flag==2:
        print("%d nao eh primo" %n)