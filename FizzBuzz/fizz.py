data = input()
data = data.split()

i = 1
while i <= int(data[2]):
	val1 = int(data[0])
	val2 = int(data[1])
	if i % val1 == 0 and i % val2 == 0:
		print('FizzBuzz')
	elif i % val1 == 0:
		print('Fizz')
	elif i % val2 == 0:
		print('Buzz')
	else:
		print(i)
	i += 1