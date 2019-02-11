while True:
    try:
        n = int(input())

        ar = [int(n) for n in input("").split()]
        maxSpeed = max(ar)
        if maxSpeed < 10:
            print(1)
        elif maxSpeed >= 10 and maxSpeed < 20:
            print(2)
        else:
            print(3)
    except EOFError:
            break
