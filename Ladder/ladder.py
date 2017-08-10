import math

input = input()
data = input.split()

h = int(data[0])
v = int(data[1])
l = (h/math.sin(math.radians(v)))

print(str(math.ceil(l)))