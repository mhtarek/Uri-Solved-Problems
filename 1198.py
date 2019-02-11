while True:
    try:
        ar = [int(i) for i in input().split()]
        dif = abs(ar[0] - ar[1])
        print(dif)

    except EOFError:
        break