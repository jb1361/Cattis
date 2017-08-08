
monthlydata = int(input())
months = int(input())
dataused = []
i = 0
while i < months:
	dataused.append(int(input()))
	i+=1

nextmonthsdata = (monthlydata * months) + monthlydata
for i in dataused:
	nextmonthsdata -= i

output = nextmonthsdata
print(output)