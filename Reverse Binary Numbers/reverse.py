number = input()
binarynum = bin(int(number))[2:]
output = binarynum[::-1]
output = int(output,2)
print(output)

