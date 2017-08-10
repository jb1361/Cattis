statues = int(input())

def counter(n):
	counter = 0
	while(n-1):
		counter += 1
		n >>= 1
	return counter

def days(i):
	#return i < 4 ? i : i and (i - 1) ? counter(i<<1 + 1) : counter(i) + 1
	return i if i < 4 else i and (i - 1) if counter(i<<1 + 1) else counter(i) + 1
			
			
print(days(statues))

#doesnt work currently this is quite difficult (may not be, I just don't know how its supposed to work)