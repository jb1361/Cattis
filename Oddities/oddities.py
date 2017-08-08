iterations = int(input())
data = []
i = 0
while i < iterations:
	data.append(int(input()))
	i+=1
	
for i in data:
	if (i % 2 == 0):
		print(str(i) + ' is even')
	else:
		print(str(i) + ' is odd')
