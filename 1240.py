n = int(input())
for j in range(n):
    ar = [i for i in input().split()]

    if ar[1] in ar[0]:
        print('encaixa')
    else:
        print('nao encaixa')

