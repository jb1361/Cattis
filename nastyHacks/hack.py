cases = int(input())
output = []

def compute(n):
	revenue = int(n[0])
	revenue_advertise = int(n[1])
	advertise_cost = int(n[2])
	advertise_profit = revenue_advertise-advertise_cost
	if advertise_profit == revenue:
		output.append('does not matter')
	if advertise_profit > revenue:
		output.append('advertise') 
	if advertise_profit < revenue:
		output.append('do not advertise') 
while cases > 0:
	n = input()
	n = n.split()
	compute(n)
	cases -= 1

for i in output:
	print(i)