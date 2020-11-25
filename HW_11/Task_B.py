from sys import stdin, stdout

INF = 10 ** 8
START = 0

n, m = map(int, stdin.readline().split())
adjacency_list = [list() for i in range(n)]
for i in range(m):
	u, v, w = map(int, stdin.readline().split())
	u -= 1
	v -= 1
	adjacency_list[u].append((v, w))
	adjacency_list[v].append((u, w))

distance = [INF] * n
distance[START] = 0
my_set = set()
my_set.add((0, START))
for i in range(n):
	if len(my_set) == 0:
		break
	next = min(my_set, key = lambda x: x[0])
	my_set.discard(next)
	for u in adjacency_list[next[1]]:
		if distance[u[0]] > distance[next[1]] + u[1]:
			my_set.discard((distance[u[0]], u[0]))
			distance[u[0]] = min(distance[u[0]], distance[next[1]] + u[1])
			my_set.add((distance[u[0]], u[0]))

stdout.write(' '.join(map(str, distance)))