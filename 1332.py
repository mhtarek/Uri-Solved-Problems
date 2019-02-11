for i in range(int(input())):
    n = input()

    if len(n)==5:
        print(3)
    elif (n[0]=='t' and n[1]=='w') or (n[1]=='w' and n[2]=='o') or (n[0]=='t' and n[2]=='o'):
        print(2)
    else:
        print(1)