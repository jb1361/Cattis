g = input()
e = input()
g = g.split()
e = e.split()
g_max_total = 0
e_max_total = 0
gd1_diff = 0
gd2_diff = 0
ed1_diff = 0
ed2_diff = 0





gd1_diff = (int(g[1]) + int(g[0])) - 1
gd2_diff = (int(g[3]) + int(g[2])) - 1
ed1_diff = (int(e[1]) + int(e[0])) - 1
ed2_diff = (int(e[3]) + int(e[2])) - 1
g_max_total = gd1_diff + gd2_diff
e_max_total = ed1_diff + ed2_diff


if g_max_total == e_max_total:
	print('Tie')
elif g_max_total > e_max_total:
	print('Gunnar')
else:
	print('Emma')