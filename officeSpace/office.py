output = []
data = []
employee_rects = []
grid = [][]
def populate_grid(x,y):
	for i in range(0,x):
		
	
def compute_areas(area):
	max_area = (int(area[0]) * int(area[1]))
	output.append('Total ' + str(max_area))
	unallocated = 0
	contested = 0
	output.append('Unallocated ' + str(unallocated))
	output.append('Contested ' + str(contested))
	populate_grid(int(area[0]),int(area[1]))
		
def get_employee_requests(area,i):
	#global employee_rects
	
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
		get_employee_requests(area,test_cases)
	except:
		break;


for i in output:
	print(i)