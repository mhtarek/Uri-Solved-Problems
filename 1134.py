n=0
al=0
gas=0
di=0
while(True):
    n=eval(input())
    if n==1:
        al=al+1
    elif n==2:
        gas=gas+1
    elif n==3:
        di=di+1
    elif n==4:
        break
print("MUITO OBRIGADO")
print("Alcool: ",al)
print("Gasolina: ",gas)
print("Diesel: ",di)