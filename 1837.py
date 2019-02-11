
ar = [int(i) for i in input().split()]

q = ar[0] // ar[1]
r = ar[0] % ar[1]
if (r < 0):
    if (q < 0):
        q-=1
    if (q > 0):
        q+=1
    r=ar[0]-(ar[1] * q)


print('%d %d' % (q, r))
