case = input()
case = case.split()
movement_data = []
output = []

def get_if_done(lst):
	if int(lst[0]) == 0 and int(lst[1]) == 0:
		return True

def calculate_position(RW,RL):
	bot_x = 0
	bot_y = 0
	bot_x_actual = 0
	bot_y_actual = 0
	for i in movement_data:
		temp = i.split()
		if temp[0] == 'u':
			bot_y += int(temp[1])
			bot_y_actual += int(temp[1])
			if bot_y_actual > RL:
				bot_y_actual = RL
		elif temp[0] == 'd':
			bot_y -= int(temp[1])
			bot_y_actual -= int(temp[1])
			if bot_y_actual < 0:
				bot_y_actual = 0
		elif temp[0] == 'r':
			bot_x += int(temp[1])
			bot_x_actual += int(temp[1])
			if bot_x_actual > RW:
				bot_x_actual = RW
		elif temp[0] == 'l':
			bot_x -= int(temp[1])
			bot_x_actual -= int(temp[1])
			if bot_x_actual < 0:
				bot_x_actual = 0
	output.append('Robot thinks ' + str(bot_x) + ' ' + str(bot_y))
	output.append('Actually at ' + str(bot_x_actual) + ' ' + str(bot_y_actual))
	output.append('')
	
	del movement_data[:]
		
def get_movements(i):
	j = 0
	while j < i:
		movement_data.append(input())
		j+=1
	calculate_position(int(case[0])-1,int(case[1])-1)






while get_if_done(case) != True:
	movements = int(input())
	get_movements(movements)
	case = input()
	case = case.split()

for i in output:
	print(i)

