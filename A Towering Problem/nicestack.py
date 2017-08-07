

data = input()

boxes = data.split()
tower1h = int(boxes[6])
tower2h = int(boxes[7])
boxes.remove(boxes[7])
boxes.remove(boxes[6])
tower1 = []

testtower1h = 0
for i in boxes:
	for j in boxes:
		for k in boxes:
			print(i +':'+ j +':' + k)
			if i+j+k == tower1h:
				tower1[0] = i
				tower1[1] = j
				tower1.add(k)
				#these arnt adding to the list

print(tower1)
output = data
print(output)