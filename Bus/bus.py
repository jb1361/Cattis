cases = int(input())
output = []


def compute_passengers(n,total):
	temp = (2**n) - 1
	output.append(temp)	
	
i = 0
while i < cases:
	compute_passengers(int(input()),0)
	i += 1
	
for i in output:
	print(int(i))