cases = int(input())
books_added = (cases/2) + 1
data = []
total = 0
group = []

def calc():
	global total
	global group
	group.sort()
	total = total + group[1]
	total = total + group[2]


	
i = 0
while i < cases:
	data.append(int(input()))
	i = i + 1
data.sort(reverse = True)
n = 1
for i in data:
	if n == 3:
		group.append(i)
		calc()
		n = 0	
		del group[:]
	else:
		group.append(i)
	n = n + 1

if (len(group) > 0):
	for i in group:
		total = total + i
	
print(total)