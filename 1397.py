player1,player2=0,0

while True:
    n = int(input())
    if n==0:
        break
    else:
        for i in range(n):
            ar = [int(j) for j in input().split()]
            if ar[0]>ar[1]:
                player1 += 1
            elif ar[0]<ar[1]:
                player2+=1
        print("%d %d" %(player1,player2))
    player1, player2 = 0, 0