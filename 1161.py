def fact(m):
    if m==1 or m==0:
        return 1
    else:
        return m*fact(m-1)
while True:
    try:
        ar = [int(i) for i in input("").split()]

        print(fact(ar[0])+fact(ar[1]))

    except EOFError:
        break

