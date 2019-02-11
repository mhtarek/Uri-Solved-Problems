mWon = 0
jWon = 0
while True:
    n = int(input())
    if n==0:
        break
    else:
        ar = [int(i) for i in input().split()]

        for i in range(n):
            if ar[i]==0:
                mWon+=1
            else:
                jWon+=1
    print("Mary won %d times and John won %d times" %(mWon,jWon))
    mWon=jWon=0


# another solution
#
# while True:
#     n = int(input(""))
#     if n == 0: break
#     m = len([x for x in input("").split() if x == '0'])
# print("Mary won", m, "times and John won", n - m, "times")