m = 12
sum = 0

t = input()
ar = [[0 for j in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        k = float(input())
        ar[i][j] = k

x = int((m-1)/2)

for i in range(x):
    for j in range(1+i,m-1-i):
        sum+=float(ar[i][j])

if t=='S':
    print('%.1f' %sum)
elif t =='M':
    avg = float(sum/30)
    print('%.1f' %avg)
