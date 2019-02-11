x = 12
n=int(input())
t = input()
a=[]
sum = 0
for i in range(x):
    a.append([0]*x)
    for j in range(x):
        a[i][j]=input()
        if j==n:
            sum+=float (a[i][j])


if t=='S':
    print('%.1f' %sum)
elif t =='M':
    avg = float(sum/x)
    print('%.1f' %avg)