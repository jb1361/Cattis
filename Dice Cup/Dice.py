input = input()
data = input.split()
d1 = int(data[0])
d2 = int(data[1])

def most_common(lst):
    return max(set(lst), key=lst.count)


mostcommon = []
combinations = d1 * d2
history = []
i = 1
j = 1
while i <= d1:
	j = 1
	while j <= d2:
		history.append(i+j)
		j+=1
	i+=1

mostcommon = most_common(history)
print(mostcommon)
#need to return multiple ones that have the same probability