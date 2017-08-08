loop = True
data = []
found = False
output = []


while loop == True:
	temp = input()
	if int(temp) == 0:
		loop = False
	else:	
		data.append(int(temp))

def get_sum(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s


m = 11
for i in data:
	found = False
	m = 11
	while found == False:
		temp = i * m
		temp1 = get_sum(i)
		temp2 = get_sum(temp)		
		if temp1 == temp2:			
			output.append(m)
			found = True
		else:
			m+=1

			

for i in output:
	print(i)
