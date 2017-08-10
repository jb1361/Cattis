p1 = input()
p2 = input()
p3 = input()
p1 = p1.split()
p2 = p2.split()
p3 = p3.split()

x = []
y = []

x.append(int(p1[0]))
x.append(int(p2[0]))
x.append(int(p3[0]))
y.append(int(p1[1]))
y.append(int(p2[1]))
y.append(int(p3[1]))

output = []


for i in x:
	temp = x.count(i)
	if temp != 2:
		output.append(i)
for i in y:
	temp = y.count(i)
	if temp != 2:
		output.append(i)
		
print(str(output[0])+ ' ' + str(output[1]))