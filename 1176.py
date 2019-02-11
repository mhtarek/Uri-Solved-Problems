n = int(input())
for i in range(n):
    n1 = 0
    n2 = 1
    count = 0
    li = []
    while count<= 60:
        li.append(n1)
        nth =n1+n2
        n1 = n2
        n2 = nth
        count+=1
    x = int(input())
    print("Fib(%d) = %d" %(x,li[x]))

