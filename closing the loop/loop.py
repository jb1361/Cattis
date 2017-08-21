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

def find_highest_initial(data_set):
	temp = 0
	h = ''
	for i in data_set:
		if int(i[:-1]) > temp:
			h = i
			temp = int(i[:-1])
	return h
	
def find_highest(lst,color):
	highest = ''
	temp = 0
	for i in lst:
		if int(i[:-1]) > temp and i[len(i)-1] != color:
			temp = int(i[:-1])
			highest = i
	return highest		
		
def get_next_rope(data_set,color,total_length):
	next = find_highest(data_set,color)
	highest = int(next[:-1])
	color = next[len(next)-1]
	temp_data = data_set
	temp_data.remove(next)
	if check_if_rope_possible(temp_data) == False:
		output.append('Case #' + str(case_num) + ':' + ' ' + str(total_length + (highest-1)))
	else:	
		next_total = total_length + (highest - 1)
		get_next_rope(temp_data,color,next_total)
		
		
def calculate_rope_length(total_length,color,data_set):
	initial = find_highest_initial(data_set)
	highest = int(initial[:-1])
	temp_data = data_set
	temp_data.remove(initial)
	get_next_rope(temp_data,initial[len(initial)-1],highest-1)
	

def compute_output():
	if check_if_rope_possible(data) == False:
		output.append('Case #' + str(case_num) + ':' + ' ' + str(0))
	else:
		calculate_rope_length(0,'',data)
			

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