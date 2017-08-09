cont1 = input()
cont2 = input()
cont3 = input()
cont4 = input()
cont5 = input()

cont1 = cont1.split()
cont2 = cont2.split()
cont3 = cont3.split()
cont4 = cont4.split()
cont5 = cont5.split()

cont1total = 0
cont2total = 0
cont3total = 0
cont4total = 0
cont5total = 0
totals = []
for i in cont1:
	cont1total += int(i)
	
for i in cont2:
	cont2total += int(i)
	
for i in cont3:
	cont3total += int(i)
	
for i in cont4:
	cont4total += int(i)
	
for i in cont5:
	cont5total += int(i)
	
totals.append(cont1total)	
totals.append(cont2total)
totals.append(cont3total)
totals.append(cont4total)
totals.append(cont5total)	

print(str(totals.index(max(totals))+1) + ' ' + str(max(totals)))

