num = int(input())
data = []
i = 0
while i < num:
	data.append(int(input()))
	i+=1
	
sum = 0

for i in data:
	temp = str(i)
	number = temp[:-1]
	power = temp[-1:]
	sum += (int(number)**int(power))
	
print(sum)
