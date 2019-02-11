sum = 0
j=0
k=1
while k==1:
    n = float(input())
    if n>10 or n<0:
        print("nota invalida")
    else:
        sum+=n
        j+=1
        if j ==2:
            avg = float(sum/2)
            print("media = %.2f" %avg)
            if j==2:
               while True:
                   print("novo calculo (1-sim 2-nao)")
                   x = int(input())
                   if x == 1:
                       k = 1
                       break
                   elif x == 2:
                       k = 2
                       break
                   else:
                       continue

            j =0
            sum = 0
