x = int(input())

N=[]

for i in range(0,10):
    N.append(x)
    print("N[%d] = %d" % (i,N[i]))
    x = 2* x
