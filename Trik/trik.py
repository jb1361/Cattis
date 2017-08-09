data = input()

indexofball = 1


def moveA(i):
	if i == 1:
		return 2
	if i == 2:
		return 1
	return i	
def moveB(i):
	if i == 2:
		return 3
	if i == 3:
		return 2
	return i	
def moveC(i):
	if i == 1:
		return 3
	if i == 3:
		return 1
	return i
	
for i in data:
	if i == 'A':
		indexofball = moveA(indexofball)
	if i == 'B':
		indexofball = moveB(indexofball)
	if i == 'C':
		indexofball = moveC(indexofball)
		
print(indexofball)