while True:
    ar = [int(i) for i in input().split()]
    if ar[0]==ar[1]==0:
        break
    else:
        print(ar[0]+ar[1])