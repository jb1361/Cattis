cases = int(input())	
data = []
sets = 0
output = []
def get_output():
	output.append('SET ' + str(sets))
	tempdata = []
	for i in data:
		temp = (data.index(i)+1) % 2
		if temp != 0:
			output.append(i)
	for i in data:
		temp = (data.index(i)+1) % 2
		if temp == 0:
			tempdata.append(i)
	tempdata = tempdata[::-1]
	for i in tempdata:
		output.append(i)
	del data[:]
def get_input(i):
	j = 0
	while j < i:
		data.append(input())
		j+=1		
	get_output()		


while cases != 0:
		sets += 1
		get_input(cases)
		cases = int(input())
		

for i in output:
	print(i)
