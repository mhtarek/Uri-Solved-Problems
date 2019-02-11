st_day = input().split()
st_day = int(st_day[1])

st_time = input().split(":")
st_hour = int(st_time[0])
st_min = int(st_time[1])
st_sec = int(st_time[2])

stTotalSec = (st_day*24*3600)+(st_hour*3600)+(st_min*60)+st_sec

en_day = input().split()
en_day = int(en_day[1])

en_time = input().split(":")
en_hour = int(en_time[0])
en_min = int(en_time[1])
en_sec = int(en_time[2])

enTotalSec = (en_day*24*3600)+(en_hour*3600)+(en_min*60)+en_sec

totSec = enTotalSec - stTotalSec

totDay = int(totSec/(24*3600))
totSec = totSec%(24*3600)

totHour = int(totSec/(3600))
totSec = totSec%3600

totMin = totSec/60
totSec=totSec%60

print("%d dia(s)" %totDay)
print("%d hora(s)" %totHour)
print("%d minuto(s)" %totMin)
print("%d segundo(s)"%totSec)




