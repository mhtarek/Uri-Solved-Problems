inputs = int(input())

li = [int(i) for i in input().split()]
minVal = min(li)
minValInd = li.index(min(li))
print("Menor valor: %d" %minVal)
print("Posicao: %d" %minValInd)