cases = int(input())
output = []



i = 0
while i < cases:
	line = input()
	if 'Simon says' in line:
		out = line.replace('Simon says ', '')
		print(out)
		output.append(out)
	else:
		#print()
		output.append('')
	i = i + 1
#for i in output:
	#if i == '':
	#	print()
	#else:
	#	print(i)