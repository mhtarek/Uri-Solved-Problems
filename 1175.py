N = []

for i in range(0,20):
    x = input()
    N.append(x)

NR = N[::-1]

for i in range(20):
    print("N[%d] = %s" %(i,NR[i]))