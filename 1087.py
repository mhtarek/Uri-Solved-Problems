while True:
    ar = [int(i) for i in input().split()]

    if ar[0]==ar[1]==ar[2]==ar[3]==0:
        break
    elif ar[0]==ar[2] and ar[1]==ar[3]:
        print(0)
    elif ar[0]==ar[2] or ar[1]==ar[3] or abs(ar[0]-ar[2])==abs(ar[1]-ar[3]):
        print(1)
    else:
        print(2)
        