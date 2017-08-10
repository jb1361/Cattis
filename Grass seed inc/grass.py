cost = float(input())
numberoflawns = float(input())
lawns = []
total = 0
i = 0

while i < numberoflawns:
	lawns.append(input())
	i += 1
	
for i in lawns:
	temp = i.split()
	total += (float(temp[0])* float(temp[1])) * cost
	
print(str.format('{0:.7f}',total))