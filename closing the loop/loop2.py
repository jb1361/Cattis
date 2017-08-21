cases = int(input())
output = []
case_num = 1
data = []


def check_if_rope_possible(lst):
	if len(lst) > 0:
		first_color = lst[0][len(lst[0])-1]
		for i in lst:
			if i[len(i)-1] != first_color:
				return True
	return False

def remove_lowest():
	red = 0
	blue = 0
	for i in data:
		color = i[len(i)-1]
		if color == 'R':
			red += 1
		else:
			blue += 1
	remove = ''
	
	if red > blue:
		lowest = 101
		for i in data:
			if int(i[:-1]) < lowest and i[len(i)-1] == 'R':
				lowest = int(i[:-1])
				remove = i
	else:
		lowest = 101
		for i in data:
			if int(i[:-1]) < lowest and i[len(i)-1] == 'B':
				lowest = int(i[:-1])
				remove = i
	data.remove(remove)

	calculate_rope_length()
	
def check_if_even():
	red = 0
	blue = 0
	for i in data:
		color = i[len(i)-1]
		if color == 'R':
			red += 1
		else:
			blue += 1
	if red == blue:
		return True
	else:
		return False
	
def calculate_rope_length():
	total = 0
	if check_if_even() == True:
		for i in data:
			total += int(i[:-1])-1
		output.append('Case #' + str(case_num) + ':' + ' ' + str(total))
	else:
		remove_lowest()

	

def compute_output():
	if check_if_rope_possible(data) == False:
		output.append('Case #' + str(case_num) + ':' + ' ' + str(0))
	else:
		calculate_rope_length()
			

def get_data():
	not_used = input()
	ropes = input()
	temp = ropes.split()
	for i in temp:
		data.append(i)
	compute_output()
	del data[:]
	
	
i = 0 
while i < cases:
	get_data()
	case_num += 1
	i += 1
	

for i in output:
	print(i)