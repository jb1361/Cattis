strings = int(input())*2
output = []
stringarray = []
dif = ''
i = 0
while i < strings:
	stringarray.append(input())
	i += 1

	
def get_diff(s1,s2):
	global dif		
	output.append(s1)
	output.append(s2)
	index = 0
	while index < len(s1):
		if s1[index] == s2[index]:
			dif += '.'
		else:
			dif += '*'
		index += 1
	output.append(dif)
	dif = ''
	
j = 0
while j < len(stringarray):
	string1 = stringarray[j]
	string2 = stringarray[j+1]
	get_diff(string1,string2)
	j+= 2

count = 1
for i in output:
	if count % 3 != 0:
		print(i)
	else:
		print(i)
		print()
	count += 1
	
	
	
	