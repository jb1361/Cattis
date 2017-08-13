test_cases = int(input())
hurricaneData = []
citys = []
output = []

def distance(x1,y1,x2,y2):
	i = (x2-x1)**2 + (y2-y1)**2
	return i**(1/2)

def distance_by_three_points(city_x,city_y,x1,y1,x2,y2):
		t1 = (y2-y1)*city_x
		t2 = (x2 - x1)*city_y
		t3 = (x2*y1) - (y2*x1)
		numerator = abs(t1-t2+t3)
		t4 = (y2-y1)**2 + (x2-x1)**2
		denominator = t4**(1/2)
		return numerator/denominator
		
def format_output(list):
	output.append(' '.join(x for x in list))
	
def format_output_distance(list):
	lowest = 10000
	for i in list:
		if i[1] < lowest:
			lowest = i[1]
	i = 0
	out = []
	while i < len(list):
		if list[i][1] == lowest:
			out.append(list[i][0]) 	
		i += 1
	format_output(out)
	
def get_next_y(x,slope,b):
	return (slope * x) + b
	
def get_next_x(x,slope,b):
	y = get_next_y(x,slope,b)
	return (y-b)/x
	
horiline = False	
vertline = False
def get_slope(x1,y1,x2,y2):
	global vertline
	global horiline
	vertline = False
	horiline = False
	xchange = (x2 - x1)
	ychange = (y2 - y1)
	if ychange != 0 and xchange != 0:
		return (ychange/xchange)
	elif xchange == 0:
		vertline = True
		return 0
	else:
		horiline = True
		return 0
def get_b(x,y,slope):
	return  y - (slope * x)
	
def check_if_on_line(x,y,slope,b):
	i = (slope*x) + b
	if y == i:
		return True
	else:
		return False

def check_if_on_vertical_line(x,y,city_x,city_y):
	i = 0
	while i < 1000:
		if (city_y == y+i and city_x == x):
			return True
		i+=1
		
	j = 1000
	while j > 0:
		if (city_y == y+j and city_x == x):
			return True
		j-=1
	return False
	
def check_if_on_horizontal_line(x,y,city_x,city_y):
	i = 0
	while i < 1000:
		if (city_y == y and city_x == x+i):
			return True
		i+=1
		
	j = 1000
	while j > 0:
		if (city_y == y and city_x == x+j):
			return True
		j-=1
	return False
	
def check_if_all_false_on_vertical_line(x,y):
	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		i = 0
		while i < 1000:
			if (city_y == y+i and city_x == x):
				return True
			i+=1
		j = 1000
		while j > 0:
			if (city_y == y+j and city_x == x):
				return True
			j-=1	
	return False
	
def check_if_all_false_on_horizontal_line(x,y):
	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		i = 0
		while i < 1000:
			if (city_y == y and city_x == x+i):
				return True
			i+=1
		j = 1000
		while j > 0:
			if (city_y == y and city_x == x+j):
				return True
			j-=1	
	return False
		
def check_if_all_false_on_line(slope,b):
	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		if (check_if_on_line(city_x,city_y,slope,b)) == True:
			return True
	return False
		
def compute_by_distance(x1,y1,x2,y2,slope,b):
	city_danger = []
	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		distance = distance_by_three_points(city_x,city_y,x1,y1,x2,y2)
		city_danger.append([city_data[0],distance])
	
	format_output_distance(city_danger)
	del city_danger[:]		
	del citys[:]
	del hurricaneData[:]
	
def compute_by_distance_vertical(x1,y1,x2,y2,slope,b):
	city_danger = []
	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		prev_dist = distance(x1,y1,city_x,city_y)
		new_dist = 0
		i = 0
		newx = x1
		newy = y1
		while i < 1000:
			newy+=1			
			new_dist = distance(newx,newy,city_x,city_y)
			if new_dist > prev_dist:
				break;
			else:
				prev_dist = new_dist
			i += 1
			
		prev_dist = distance(x1,y1,city_x,city_y)
		new_dist = 0
		j = 0		
		while j < 1000:
			newy-=1			
			new_dist = distance(newx,newy,city_x,city_y)
			if new_dist > prev_dist:
				break;
			else:
				prev_dist = new_dist
			j += 1
		city_danger.append([city_data[0],prev_dist])
	
	format_output_distance(city_danger)
	del city_danger[:]		
	del citys[:]
	del hurricaneData[:]

def compute_by_distance_horizontal(x1,y1,x2,y2,slope,b):
	city_danger = []
	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		prev_dist = distance(x1,y1,city_x,city_y)
		new_dist = 0
		i = 0
		newx = x1
		newy = y1
		while i < 1000:
			newx+=1			
			new_dist = distance(newx,newy,city_x,city_y)
			if new_dist > prev_dist:
				break;
			else:
				prev_dist = new_dist
			i += 1
			
		prev_dist = distance(x1,y1,city_x,city_y)
		new_dist = 0
		j = 0		
		while j < 1000:
			newx-=1			
			new_dist = distance(newx,newy,city_x,city_y)
			if new_dist > prev_dist:
				break;
			else:
				prev_dist = new_dist
			j += 1
		city_danger.append([city_data[0],prev_dist])
	
	format_output_distance(city_danger)
	del city_danger[:]		
	del citys[:]
	del hurricaneData[:]
	
def compute_by_on_line(slope,b):
	city_danger = []

	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		if (check_if_on_line(city_x,city_y,slope,b)) == True:
			city_danger.append(city_data[0])
	format_output(city_danger)
	del city_danger[:]		
	del citys[:]
	del hurricaneData[:]
	
def compute_by_on_line_vertical(x,y):
	city_danger = []

	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		if check_if_on_vertical_line(x,y,city_x,city_y) == True:
			city_danger.append(city_data[0])
	format_output(city_danger)
	del city_danger[:]		
	del citys[:]
	del hurricaneData[:]
	
def compute_by_on_line_horizontal(x,y):
	city_danger = []

	for j in citys:
		city_data = j.split()
		city_x = int(city_data[1])
		city_y = int(city_data[2])
		if check_if_on_horizontal_line(x,y,city_x,city_y) == True:
			city_danger.append(city_data[0])
	format_output(city_danger)
	del city_danger[:]		
	del citys[:]
	del hurricaneData[:]
				
def compute_output():
	temp = []
	temp = hurricaneData[0].split()
	x1 = int(temp[0])
	y1 = int(temp[1])
	x2 = int(temp[2])
	y2 = int(temp[3])
	slope = get_slope(x1,y1,x2,y2)
	b = get_b(x1,y1,slope)
	
	
	
	if vertline == True:
		if check_if_all_false_on_vertical_line(x1,y1) == False:
			
			compute_by_distance_vertical(x1,y1,x2,y2,slope,b)
		else:
			compute_by_on_line_vertical(x1,y1)
	elif horiline == True:
		if check_if_all_false_on_horizontal_line(x1,y1) == False:
			compute_by_distance_horizontal(x1,y1,x2,y2,slope,b)
		else:
			compute_by_on_line_horizontal(x1,y1)
	else:
		if check_if_all_false_on_line(slope,b) == False:	
			compute_by_distance(x1,y1,x2,y2,slope,b)
		else:
			compute_by_on_line(slope,b)


def gather_data():
	hurricaneData.append(input())
	num_citys = int(input())
	temp = 0
	while temp < num_citys:
		citys.append(input())
		temp += 1
	compute_output()


i = 0
while i < test_cases:
	gather_data()
	i+=1
	
for i in output:
	print(i)