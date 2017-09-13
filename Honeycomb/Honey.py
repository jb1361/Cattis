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
	
def compute(n):
	if n == 1:
		output.append(0)
	if n == 2:
		output.append(6)
	else:
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