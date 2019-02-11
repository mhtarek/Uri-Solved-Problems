A = []

for i in range(100):
    x = float(input())
    A.append(x)

for i in range(100):
    if float(A[i])<=10:
        print("A[%d] = %.1f" %(i,float(A[i])))