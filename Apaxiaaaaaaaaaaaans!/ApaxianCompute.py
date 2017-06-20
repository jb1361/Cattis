

data = input() 	  
length = len(data)

i = 0
while (i < length):
	letter = data[i:i+1]
	nextletter = data[i+1:i+2]
	if(letter == ''):
		i = length
	if(letter == nextletter):
		data = data[:i] + data[i+1:length]			
		i = i-1
		
	i = i + 1
	
print(data)