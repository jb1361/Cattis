n = input()
n = n.split()
n.sort()




if (int(n[0]) == 0 and int(n[1]) == 0):
	print('Not a moose')
elif(int(n[0]) != int(n[1])):	
	num = 2*int(n[1])
	print('Odd ' + str(num))
elif(int(n[0]) == int(n[1])):
	num = int(n[0]) + int(n[1])
	print('Even ' + str(num))
	
	
	
