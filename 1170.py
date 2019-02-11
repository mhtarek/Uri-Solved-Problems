x = int(input())
for i in range(x):
    n = float(input())
    day = 0
    while n>1:
        n /= 2
        day += 1

    print("%d dias" %day)
