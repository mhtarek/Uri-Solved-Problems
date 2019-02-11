while True:
    ar = [int(i) for i in input().split()]
    if ar[0]==ar[1]==0:
        break
    else:
        c = (2*ar[0])-ar[1]
        print(c)
