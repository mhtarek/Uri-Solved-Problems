import math
while True:
    n = [int(i) for i in input("").split()]
    if n[0]==0:
        break
    else:
        x = float((n[0]*n[1]*100)/n[2])
        x = int(math.sqrt(x))
    print(x)