matchesandbox = input()
matchesandbox = matchesandbox.split()
matches = []

i = 0
while i < int(matchesandbox[0]):
	temp = input()
	matches.append(temp)
	i += 1

	
diagonallength = (int(matchesandbox[1])**2 + int(matchesandbox[2])**2) ** (1/2)

for i in matches:
	if int(i) <= diagonallength:
		print('DA')
	else:
		print('NE')