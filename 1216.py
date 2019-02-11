sum = 0
count = 0

while True:
    try:
        input()
        sum+=int(input())
        count+=1
    except EOFError:
        avg = float(sum/count)
        print("%.1f" % avg)
        break
