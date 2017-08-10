string = input()
days = 0


i = 0
while i < len(string):
	temp = string[i:i+3]
	if temp[0] != 'P':
		days += 1
	if temp[1] != 'E':
		days += 1
	if temp[2] != 'R':
		days += 1
	i += 3
print(days)