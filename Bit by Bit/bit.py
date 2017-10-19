from enum import Enum
commands = []
output = []
register = []

class Bit(Enum):
	one = 1
	zero = 0
	unknown = '?'

def format_output():
	global register
	string = ''
	register = register[::-1]
	for i in register:
		string = string + str(i)
	output.append(string)
	
def compare_OR(i,j):
	if(i == 1 or j == 1):
		return Bit.one.value
	elif(i == 0 and j == 0):
		return Bit.zero.value
	else:
		return Bit.unknown.value
def compare_AND(i,j):
	if(i == 1 and j == 1):
		return Bit.one.value
	elif(i == 0 or j == 0):
		return Bit.zero.value
	else:
		return Bit.unknown.value
		
def compute():
	for i in range(0,32):
		register.append(Bit.unknown.value)
	for j in commands:
		com = j.split()
		if (com[0] == 'CLEAR'):
			register[int(com[1])] = Bit.zero.value
		if(com[0] == 'SET'):
			register[int(com[1])] = Bit.one.value
		if(com[0] == 'OR'):
			register[int(com[1])] = compare_OR(register[int(com[1])],register[int(com[2])])
		if(com[0] == 'AND'):
			register[int(com[1])] = compare_AND(register[int(com[1])],register[int(com[2])])
	format_output()

def get_commands(i):
	while i > 0:
		commands.append(input())
		i-=1
	compute()
	del commands[:]
	del register[:]
n = int(input())
while n != 0:
	get_commands(n)
	n = int(input())


for i in output:
	print(i)