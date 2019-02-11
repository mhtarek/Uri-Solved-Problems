par=[]
impar = []
p = 0
im = 0
for i in range(15):
    value = int(input())
    if value%2==0:
        par.insert(p,value)
        p+=1
        if p==5:
            for j in range(5):
                print("par[%d] = %d" %(j,par[j]))
                par[j] = ''
            p=0
    elif value % 2 ==1:
        impar.insert(im,value)
        im+=1
        if im==5:
            for j in range(5):
                print("impar[%d] = %d" %(j,impar[j]))
                impar[j] = ''
            im=0

for i in range(5):
    if impar[i]=='':
        break
    else:
        print("impar[%d] = %d" % (i, impar[i]))

for i in range(5):
    if par[i]=='':
        break
    else:
        print("par[%d] = %d" % (i, par[i]))