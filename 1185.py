m = 12
sum = 0

t = input()
ar = [[0 for j in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        k = float(input())
        ar[i][j] = k

for i in range(0,m-1):
    for j in range(m-i-1):
        sum+=float(ar[i][j])

if t=='S':
    print('%.1f' %sum)
elif t =='M':
    avg = float(sum/66)
    print('%.1f' %avg)
