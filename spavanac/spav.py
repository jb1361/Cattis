time = input()
time = time.split()

hour = int(time[0])
minute = int(time[1])

timetosub = 45

if minute-timetosub < 0:
	if (hour - 1) >= 0:	
		hour -= 1
	else:
		hour = 23
	timetosub = timetosub-minute
	minute = 60
	minute-=timetosub
else:
	minute-=timetosub
print(str(hour) + ' ' + str(minute))