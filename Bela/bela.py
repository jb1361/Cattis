dominant = [['A',11],['K',4],['Q',3],['J',20],['T',10],['9',14],['8',0],['7',0]]
notdominant = [['A',11],['K',4],['Q',3],['J',2],['T',10],['9',0],['8',0],['7',0]]

inp = input()
inp = inp.split()
hands = int(inp[0]) * 4
domHand = inp[1]

card_data = []
i = 0


while i < hands:
	temp = input()
	card_data.append(temp)
	i += 1

	
points = 0

def calc_points(card, suit):
	if suit == domHand:
		tempp = 0
		for i in dominant:
			if i[0] == card:
				return int(i[1])
	else:
		for i in notdominant:
			if i[0] == card:
				return int(i[1])




for i in card_data:
	points += calc_points(i[0],i[1])
	
print(points)