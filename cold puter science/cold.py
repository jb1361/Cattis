notused = input()
temps = input()
tempslist = temps.split()
total = 0
for i in tempslist:
	if (int(i) < 0):
		total += 1
		
print(total)