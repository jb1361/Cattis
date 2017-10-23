output = []
data = []
employee_rects = []
grid = [[]]
def populate_grid(x,y):
	global grid
	grid = [['unallocated' for i in range(y)] for j in range(x)]

def insert_cubicle(name,x1,y1,x2,y2):
	global grid
	for i in range(x1,x2):	
		for j in range(y1,y2):
			if (grid[i][j] != 'unallocated'):
				grid[i][j] = 'contested'
			else:	
				grid[i][j] = name
				
def compute_areas(area):
	global grid
	max_area = (int(area[0]) * int(area[1]))
	output.append('Total ' + str(max_area))
	unallocated = 0
	contested = 0
	populate_grid(int(area[0]),int(area[1]))
	names = []
	for i in employee_rects:
		name = i[0]
		names.append([name,0])
		x1 = int(i[1])
		y1 = int(i[2])
		x2 = int(i[3])
		y2 = int(i[4])
		insert_cubicle(name,x1,y1,x2,y2)
	for i,r in enumerate(grid):	
		for j,element in enumerate(r):
			if(element == 'unallocated'):
				unallocated = unallocated + 1
			elif(element == 'contested'):
				contested = contested + 1
			else:
				for k in names:
					if element == k[0]:
						k[1] += 1
						
	output.append('Unallocated ' + str(unallocated))
	output.append('Contested ' + str(contested))
	for i in names:
		output.append(str(i[0]) + ' ' + str(i[1]))
	output.append('')
	
def get_employee_requests(area,i):
	while i > 0:
		e = input()
		e = e.split()
		employee_rects.append(e)
		i-=1
	compute_areas(area)
				
while (True):
	try:
		area = input()
		area = area.split()
		test_cases = int(input())
		del employee_rects[:]
		get_employee_requests(area,test_cases)
	except:
		break;


for i in output:
	print(i)