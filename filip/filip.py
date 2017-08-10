input = input()
data = input.split()
first = 0
second = 0
first = int(data[0][::-1])
second = int(data[1][::-1])
if first > second:
	print(first)
else:
	print(second)