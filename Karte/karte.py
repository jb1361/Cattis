data = input()
output = []
n = 3
data = [data[i:i+n] for i in range(0, len(data), n)]


def duplicates(l):
	for i in l:
		if i > 1:
			return True
			break;
	return False
	
def compute():	
	check_duplicates = {x:data.count(x) for x in data}
	check_duplicates = check_duplicates.values()
	if(duplicates(check_duplicates) == False):
		P = 13
		K = 13
		H = 13
		T = 13
		for i in data:
			suit = i[0]
			if (suit == 'P'):
				P-=1
			if (suit == 'K'):
				K-=1
			if (suit == 'H'):
				H-=1
			if (suit == 'T'):
				T-=1
		output.append(str(P) + ' ' + str(K) + ' ' + str(H) + ' ' + str(T))
	else:
		output.append('GRESKA')
		
compute()
print(output[0])



