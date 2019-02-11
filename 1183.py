t = input()
m = 12
sum = 0
ar = [[0 for j in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        k = float(input())
        ar[i][j] = k

for i in range(m):
    for j in range(i+1,m):
        sum+=float(ar[i][j])

if t=='S':
    print('%.1f' %sum)
elif t =='M':
    avg = float(sum/66)
    print('%.1f' %avg)
