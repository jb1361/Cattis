l = int(input())
d = int(input())
x = int(input())


def get_sum_of_digits(num):
	total = 0
	for i in str(num):
		total += int(i)
		
	return total


def get_min(l,d,x):
	i = l
	while i <= d:
		sum = get_sum_of_digits(i)
		if sum == x:
			print(i)
			break;
		i+=1


def get_max(l,d,x):		
	i = d
	while i >= l:
		sum = get_sum_of_digits(i)
		if sum == x:
			print(i)
			break;
		i-=1

get_min(l,d,x)
get_max(l,d,x)