led=0
for i in range(int(input())):
    st = input()
    for i in range(len(st)):
        if st[i]=='1':
            led+=2
        elif st[i]=='2' or st[i]=='3' or st[i]=='5':
            led+=5
        elif st[i] == '4':
            led += 4
        elif st[i] == '6' or st[i]=='9' or st[i]=='0':
            led += 6
        elif st[i] == '7':
            led += 3
        elif st[i] == '8':
            led += 7
    print("%d leds" %led)
    led = 0




