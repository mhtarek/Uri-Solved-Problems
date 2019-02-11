while True:
    try:
        ar = [int(i) for i in input().split()]
        d = 2 * ar[0] * ar[1]

        print(d)
    except EOFError:
        break