import math
cases = int(input())
cannon_data = []
output = []
g = 9.81
i = 0
while i < cases:
	cannon_data.append(input())
	i+=1
	
for i in cannon_data:
	data = i.split()
	v = float(data[0])
	theta = float(data[1])
	x = float(data[2])
	h1 = float(data[3])
	h2 = float(data[4])
	t = (x/(v*math.cos(math.radians(theta))))
	x_dist = (v*t*math.cos(theta))
	y = (v*t*math.sin(math.radians(theta))) - ((1/2)*(g*t**2))
	if y > (h1+1) and y < (h2-1):
		output.append('Safe')
	else:
		output.append('Not Safe')

for i in output:
	print(i)