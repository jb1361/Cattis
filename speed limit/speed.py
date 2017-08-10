data = []
output = []

def print_output():
	for i in output:
		print(str(i) + ' ' + 'miles')
		
def compute_output():
	temp = []
	totalMiles = 0
	previousTime = 0
	for i in data:
		temp.append(i.split())
	for i in temp:
		time = (int(i[1])-previousTime)
		totalMiles += (int(i[0])*time)
		previousTime = int(i[1])
		
	output.append(totalMiles)
	del data[:]
	
def gather_input(x):
	temp = 0
	while temp < int(x):
		data.append(input())
		temp+=1
	compute_output()

loop = True
while loop == True:
	inp = int(input())
	if inp == -1:
		loop = False
		break
	else:
		gather_input(inp)	
		
print_output()