cases = int(input())
data = []
output = []

def compute_turtles(inp):
	temp = inp.split()
	non_zanzi_born = 0
	i = 0
	while i < len(temp)-1:
		predicted = int(temp[i])*2
		if temp[i+1]:
			if int(temp[i+1]) > predicted:
				non_zanzi_born += int(temp[i+1]) - predicted
		i+=1
	output.append(non_zanzi_born)	

i = 0 
while i < cases:
	compute_turtles(input())
	i+=1
for i in output:
	print(i)