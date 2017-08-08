data = input()
data = data.split('-')
output = ''
for i in data:
	output += i[:1]

print(output)