data = input()
data = data.split()
data.sort( reverse=True)
if data[0] > data[1]:
	data[0] = data[1]

if data[2] > data[3]:
	data[2] = data[3]

area = int(data[0]) * int(data[2])
print(area)