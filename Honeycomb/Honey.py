import math
cases = int(input())
data = []
output = []
i = 0
while i < cases:
	data.append(input())
	i+=1
"""
Try adding combs * 3 from all previous layers
or go back to just calculating tracks based on n with formulas
"""
"""
def calculate(prev, i, n):
	if i < n:
		if (i % 2)  == 0:
		#	max_layer = math.floor(i/2)
			#combs_at_max_layer = 6 * ((2**max_layer)-1)
			next = (prev * 3)
			return calculate(next,i+1,n)
		elif (i % 2) != 0:
			
			next = prev * 5
			return calculate(next,i+1,n)
	else:
		
		return prev
	"""
def calc_combs(layer):
	return (6 * (2**(layer-1)))
	
	
	
def calculate(n):
	total = 6
	if (n % 2)  == 0:
		max_layer = math.floor(n/2)
		combs_at_max_layer = calc_combs(max_layer)
		combs_two_ways = combs_at_max_layer/2
		top_layer_ways = (combs_two_ways * 2)+combs_two_ways
		total += top_layer_ways
		middle_layers = max_layer - 1
		if (math.fabs(middle_layers) > 0):
			i = 0
			layer = max_layer - 1 
			middle_ways = 0
			while i < (middle_layers):
				combs_at_layer = calc_combs(layer)
				ways_at_layer = (combs_at_layer * 6) + (combs_at_layer * 5)
				middle_ways += ways_at_layer
				i += 1
			total += middle_ways
				
	elif (n % 2) != 0:
		max_layer = math.floor(n/2)
		combs_at_max_layer = calc_combs(max_layer)
		combs_two_ways = combs_at_max_layer/2
		top_layer_ways = (combs_two_ways * 4)+(combs_two_ways*3)
		total += top_layer_ways
		middle_layers = max_layer - 1
		
		if (math.fabs(middle_layers) > 0):
			i = 0
			layer = max_layer - 1 
			middle_ways = 0
			while i < (middle_layers):
				combs_at_layer = calc_combs(layer)
				ways_at_layer = (combs_at_layer * 6) * 2
				middle_ways += ways_at_layer
				i += 1
			total += middle_ways





		
	return total

def compute(n):
	if n == 1:
		output.append(0)
	if n == 2:
		output.append(6)
	if n == 3:
		output.append(18)
	if n > 3:
		out = calculate(n)
		output.append(out)
		
def start():
	n = 0
	for i in data:
		n = i
		compute(int(n))
		
start()

for i in output:
	print(int(i))