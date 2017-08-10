test_cases = int(input())

hurricaneData = []
citys = []
output = []






def compute_output():
	temp = []
	temp = hurricaneData[0].split()
	x1 = int(temp[0])
	y1 = int(temp[1])
	x2 = int(temp[2])
	y2 = int(temp[3])
	xchange = (x2 - x1)
	ychange = (y2 - y1)
	if ychange != 0:
		slope = xchange/ychange
	else:
		slope = xchange
	print(slope)
	i = 0
	newx = x2
	newy = y2
	while i < 100:
		print('Predicted Path: ' + str(newx + xchange) + ',' + str(newy+ychange))
		newx += xchange
		newy += ychange
		i += 1
	
	del citys[:]
	del hurricaneData[:]
	


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
	print(output)