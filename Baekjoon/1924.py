dayname = ['SUN','MON','TUE','WED','THU','FRI','SAT']
molength = [31,28,31,30, 31,30,31,31, 30,31,30,31]


month,day = input().split()

month = int(month)
day = int(day)

sumdate = 0
for n in range(1,month):
    sumdate += molength[n-1]

sumdate += day

dayidx = int(sumdate%7)

print(dayname[dayidx])
