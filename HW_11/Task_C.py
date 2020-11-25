NO_EDGE = 100 * 10000 + 1
MAX_EDGE = 10000

def get_cycle(n, next, start):
	cycle = list()
	cur = start
	cycle.append(cur)
	while next[cur][start] != start and len(cycle) <= n:
		cur = next[cur][start]
		cycle.append(cur)
	return cycle


distance = list()
n = int(input())
for i in range(n):
	row = list(map(int, input().split()))
	row = [x if x <= MAX_EDGE else NO_EDGE for x in row]
	distance.append(row)

next = list()
for i in range(n):
	next.append(list(range(n)))

for k in range(n):
	for u in range(n):
		for v in range(n):
			if distance[u][v] > distance[u][k] + distance[k][v] and distance[u][k] + distance[k][v] > -NO_EDGE:
				distance[u][v] = distance[u][k] + distance[k][v]
				next[u][v] = next[u][k]

cycle = list()
for i in range(n):
	if distance[i][i] < 0:
		cycle = get_cycle(n, next, i)
		while len(cycle) > n:
			cycle = get_cycle(n, next, cycle[-1])
		break

if len(cycle) > 0:
	print('YES')
	print(len(cycle))
	print(' '.join([str(x + 1) for x in cycle]))
else:
	print('NO')