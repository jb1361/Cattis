

data = input()

boxes = data.split()
tower1h = int(boxes[6])
tower2h = int(boxes[7])
boxes.remove(boxes[7])
boxes.remove(boxes[6])
tower1 = []
tower2 = []
for i in boxes:
	for j in boxes:
		for k in boxes:
			if i != j and i != k and j != k:
				if int(i)+int(j)+int(k) == tower1h:			
					tower1.append(int(i))
					tower1.append(int(j))
					tower1.append(int(k))
					break
		if tower1:
			break
	if tower1:
		break

tower1.sort(reverse = True)
boxes.remove(str(tower1[0]))
boxes.remove(str(tower1[1]))
boxes.remove(str(tower1[2]))
tower2.append(int(boxes[0]))
tower2.append(int(boxes[1]))
tower2.append(int(boxes[2]))
tower2.sort(reverse = True)


output = str(tower1[0]) + ' ' + str(tower1[1]) + ' ' + str(tower1[2]) + ' ' + str(tower2[0]) + ' ' + str(tower2[1]) + ' ' + str(tower2[2])
print(output)