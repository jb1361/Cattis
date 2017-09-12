cases = int(input())
data = []
output = []
i = 0

while i < cases:
	data.append(input())
	i += 1
	
for i in data:
	data_set = i.split()
	name = data_set[0]
	post_secondary = data_set[1]
	post_secondary = post_secondary.split('/')
	post_secondary = int(post_secondary[0])
	dob = data_set[2]
	dob = dob.split('/')
	dob = int(dob[0])
	courses = int(data_set[3])
	
	if post_secondary >= 2010 or dob >= 1991:
		output.append(str(name) + ' ' + 'eligible')
	elif courses >= 41:
		output.append(str(name) + ' ' + 'ineligible')
	else:
		output.append(str(name) + ' ' + 'coach petitions')
		
		
		
for i in output:
	print(i)