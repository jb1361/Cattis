cases = int(input())
data = []
data_parsed = []
data_counted = []
output = []



def compute():
	total = 0
	for i in data_counted:
		num = int(i[1])
		total += num**len(data_counted)
	output.append(total)
	del data[:]
	del data_parsed[:]
	del data_counted[:]
	
def check_if_in(p):
	for i in data_counted:	
		if p == i[0]:
			return True		
	return False

def count_data():
	for i in data:
		piece = i[1]
		if len(data_counted) > 0:
			if (check_if_in(piece) == True):
				current = 0
				while current < len(data_counted):
					if piece == data_counted[current][0]:
						temp = data_counted[current][1]
						temp = int(temp) + 1
						data_counted.remove(data_counted[current])
						data_counted.append([piece,temp])
						current = len(data_counted)
					else:
						current + 1
			elif(check_if_in(piece) == False):
				data_counted.append([piece,1])
		else:
			data_counted.append([piece,1])
	compute()
	
def get_data(n):
	i = 0 
	while i < n:
		data.append(input().split())
		i += 1
	count_data()
i = 0
while i < cases:
	values = int(input())
	get_data(values)
	i += 1
	
for i in output:
	print(i)


