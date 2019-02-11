dir = ['N','L','S','O']
while True:
    n = int(input())
    if n==0:
        break
    else:
        x = sum([1 if x == 'D' else -1 for x in input("")])
        x%=4
    print(dir[x])