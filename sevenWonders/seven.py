n = input()

T = 0
C = 0
G = 0

for i in n:
	if i == 'T':
		T+=1
	if i == 'C':
		C+=1
	if i == 'G':
		G+=1

l = []
l.append(T)
l.append(C)
l.append(G)
l.sort()
sets = l[0]
points = (T**2) + (C**2) + (G**2) + (sets * 7)

print(points)	