n = []
x = int(input())
z=0

for y in range(1000):
    print("N[%d] = %d" %(y,z))
    z+=1
    if z==x:
        z=0
