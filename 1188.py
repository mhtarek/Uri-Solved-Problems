m = 12
sum = 0
t = input()
ar = [[0 for j in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        k = float(input())
        ar[i][j] = k

p=5
q=6

for i in range(7,m):
    for j in range(p,q+1):
        sum+=float(ar[i][j])
    q+=1
    p-=1


if t=='S':
    print('%.1f' %sum)
elif t =='M':
    avg = float(sum/30)
    print('%.1f' %avg)
