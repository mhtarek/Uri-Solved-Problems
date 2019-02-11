#100, 50, 20, 10, 5, 2,1, 0.50, 0.25, 0.10, 0.05, 0.01
#10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1

n = float(input())
n =int(n*100)

n1 =n/10000
n =n%10000

n2 =n/5000
n =n%5000

n3 =n/2000
n =n%2000

n4 =n/1000
n =n%1000

n5 =n/500
n =n%500

n6 =n/200
n =n%200

n7 =n/100
n =n%100

n8 =n/50
n =n%50

n9 =n/25
n =n%25

n10 =n/10
n =n%10

n11 =n/5
n =n%5

n12 =n/1
n =n%1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %n1)
print("%d nota(s) de R$ 50.00" %n2)
print("%d nota(s) de R$ 20.00" %n3)
print("%d nota(s) de R$ 10.00" %n4)
print("%d nota(s) de R$ 5.00" %n5)
print("%d nota(s) de R$ 2.00" %n6)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %n7)
print("%d moeda(s) de R$ 0.50" %n8)
print("%d moeda(s) de R$ 0.25" %n9)
print("%d moeda(s) de R$ 0.10" %n10)
print("%d moeda(s) de R$ 0.05" %n11)
print("%d moeda(s) de R$ 0.01" %n12)



