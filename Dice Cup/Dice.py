input = input()
data = input.split()
d1 = int(data[0])
d2 = int(data[1])


combinations = d1 * d2
history = []
i = 1
j = 1
while i <= d1:
	j = 1
	while j <= d2:
		history.append(i+j)
		j+=1
	i+=1
	
	
	
def contains(lst,num):
	for i in lst:
		if num is i[0]:
			return True
	return False	
		
historycounts = []
for i in history:
	if contains(historycounts,i) == False:
		historycounts.append([i,history.count(i)])

historycounts.sort(key = lambda x: x[1], reverse = True)

output = []
index = 0
for i,j in historycounts:
	output.append(i)	
	if j != historycounts[index+1][1]:
		break
	else:
		index += 1
output.sort()
for i in output:
	print(i)


