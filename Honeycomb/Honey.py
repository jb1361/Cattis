import math
cases = int(input())
data = []
output = []
i = 0
while i < cases:
	data.append(input())
	i+=1
	
"""	
def calculate_greater_than_three(n):
	max_layer = math.floor(n/2)
	moves_at_max = (6*(2**(max_layer-1)))*3
	intermediate_moves = 5 *(6*)
	return_moves = (6 * max_layer)
	out = moves_at_max + return_moves
	output.append(out)
	
def calculate(n):
	max_layer = math.floor(n/2)
	moves_at_max = (6*(2**(max_layer-1)))*3
	return_moves = (6 * max_layer)
	out = moves_at_max + return_moves
	output.append(out)
	"""
def calculate(prev, i, n):
	
	if i < n:
		if (i % 2)  == 0:
			
			max_layer = math.floor(i/2)
			combs_at_next_layer = 6 * (2**max_layer)
			next = (prev * 5) - combs_at_next_layer
			return calculate(next,i+1,n)
		elif (i % 2) != 0:
			
			next = prev * 5
			return calculate(next,i+1,n)
	else:
		
		return prev
	
def compute(n):
	if n == 1:
		output.append(0)
	elif n == 2:
		output.append(6)
	elif n > 2:
		out = calculate(6,2,n)
		output.append(out)
def start():
	n = 0
	for i in data:
		n = i
		compute(int(n))
		
start()

for i in output:
	print(i)