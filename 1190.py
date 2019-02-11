m = 12
sum = 0

t = input()
ar = [[0 for j in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        k1 = float(input())
        ar[i][j] = k1
for i in range(11,0,-1):
    for j in range(11,0,-1):
        if j>i and j>11-i:
            sum+=ar[i][j]


if t=='S':
    print('%.1f' %sum)
elif t =='M':
    avg = float(sum/30)
    print('%.1f' %avg)
