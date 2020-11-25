DOWN = 'D'
RIGHT = 'R'
START = ''

n, m = map(int, input().split(' '))
cells = []
for i in range(n):
	row = map(int, input().split(' '))
	cells.append(list(row))

money = []
way = []
for i in range(n):
	money.append([])
	way.append([])
	for j in range(m):
		if i == 0 and j == 0:
			money[i].append(cells[i][j])
			way[i].append(START)
		elif i > 0 and j == 0:
			money[i].append(money[i - 1][j] + cells[i][j])
			way[i].append(DOWN)
		elif i == 0 and j > 0:
			money[i].append(money[i][j - 1] + cells[i][j])
			way[i].append(RIGHT)
		else:
			if money[i - 1][j] > money[i][j - 1]:
				money[i].append(money[i - 1][j] + cells[i][j])
				way[i].append(DOWN)
			else:
				money[i].append(money[i][j - 1] + cells[i][j])
				way[i].append(RIGHT)

best_way = []
cur_cell = [n - 1, m - 1]
cur_side = way[n - 1][m - 1]
while cur_side != START:
	best_way.append(cur_side)
	if cur_side == DOWN:
		cur_cell[0] -= 1
	else:
		cur_cell[1] -= 1
	cur_side = way[cur_cell[0]][cur_cell[1]]
best_way = best_way[::-1]

print(money[-1][-1])
print(''.join(best_way))