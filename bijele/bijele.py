data = input()
data = data.split()

kingtoadd = (1-int(data[0]))
queentoadd = (1-int(data[1]))
rooktoadd = (2-int(data[2]))
bishoptoadd = (2-int(data[3]))
knighttoadd = (2-int(data[4]))
pawntoadd = (8-int(data[5]))

print(str(kingtoadd) + ' ' + str(queentoadd) + ' '+ str(rooktoadd) + ' ' + str(bishoptoadd) +' ' + str(knighttoadd) + ' ' + str(pawntoadd))