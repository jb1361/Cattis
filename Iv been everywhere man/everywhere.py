testcases = int(input())
output = []


def get_citys(i):
	j = 0
	temp = []
	while j < int(i):
		city = input()
		if city not in temp:
			temp.append(city)
		j+=1	
	output.append(len(temp))

i = 0
while i < testcases:
	trips = input()
	get_citys(trips)
	i += 1

for i in output:
	print(i)
