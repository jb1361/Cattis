
word = input()

for i,e in enumerate(word):
	try:
		if word[i+1]: 
			if e == 's' and word[i+1] == 's':
				print('hiss')
				break
	except:	
		print('no hiss')	