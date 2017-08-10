
data = []
i = 0

while i < 10:
	data.append(input())
	i+=1

output = []
for i in data:
	temp = int(i) % 42
	if temp not in output:
		output.append(temp)

	
print(len(output))