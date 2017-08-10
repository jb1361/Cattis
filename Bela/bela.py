dominant = [['A',11],['K',4],['Q',3],['J',20],['T',10],['9',14],['8',0],['7',0]]
notdominant = [['A',11],['K',4],['Q',3],['J',2],['T',10],['9',0],['8',0],['7',0]]

inp = input()
inp = inp.split()
hands = int(inp[0]) * 4
domHand = inp[1]

data = []
i = 0
while i < hands:
	temp = input()
	data.append(temp)
	i += 1
print(data)