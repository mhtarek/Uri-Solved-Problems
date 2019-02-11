def fun(a,b):
    if a=='tesoura' and (b=='papel' or b=='lagarto'):
        return 1
    elif a=='papel' and (b=='pedra' or b=='Spock'):
        return 1
    elif a=='pedra' and (b=='lagarto' or b=='tesoura'):
        return 1
    elif a=='lagarto' and (b=='Spock' or b=='papel'):
        return 1
    elif a=='Spock' and (b=='tesoura' or b=='pedra'):
        return 1

def main():
    n = int(input())

    for i in range(1,n+1):
        ar = [i for i in input().split()]
        if ar[0] == ar[1]:
            print('Caso #%d: De novo!' %i)
        elif fun(ar[0], ar[1]):
            print('Caso #%d: Bazinga!' %i)
        else:
            print('Caso #%d: Raj trapaceou!' %i)

main()

