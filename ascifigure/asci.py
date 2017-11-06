

data = []
output = []
def get_rows(i):
	unformatted = []
	row = []
	length = max(data, key=len)
	
	while i < len(length):
		for j in data:
			try:
				row.append(j[i])
			except:
				n = 0
		i += 1	
		unformatted.append(row)
	return unformatted
		
def compute_output():
	unformatted = get_rows(0)
	print(unformatted)
	for i in unformatted:
		i = i[::-1]
		s = ''
		for j in i:
			if j == '-':
				j = '|'
			elif(j == '|'):
				j = '-'
			
			s = s + j
		print(s)
	output.append('')
	print('=================')
	
def get_input(n):
	while n > 0:
		line = input()
		data.append(line)
		n-=1
	compute_output()



n = int(input())
while n != 0:
	get_input(n)
	n = int(input())
	
#for i in output:
#	print(i)