from collections import deque


def bfs(adjacency_list, distance, used, start):
	used[start[0]][start[1]] = (-1, -1)
	distance[start[0]][start[1]] = 0
	queue = deque()
	queue.append((start[0], start[1]))
	while len(queue) > 0:
		v = queue.popleft()
		for u in adjacency_list[v[0]][v[1]]:
			if used[u[0]][u[1]] == 0:
				used[u[0]][u[1]] = v
				distance[u[0]][u[1]] = distance[v[0]][v[1]] + 1
				queue.append(u)


N = int(input())
x1, y1 = [int(x) - 1 for x in input().split()]
x2, y2 = [int(x) - 1 for x in input().split()]

adjacency_list = list()
distance = list()
used = list()
for i in range(N):
	adjacency_list.append(list())
	distance.append([0] * N)
	used.append([0] * N)
	for j in range(N):
		adjacency_list[i].append(list())
		for x, y in zip([1, 1, 2, 2, -1, -1, -2, -2], [2, -2, 1, -1, 2, -2, 1, -1]):
			if i + x >= 0 and j + y >= 0 and i + x < N and j + y < N:
				adjacency_list[i][j].append((i + x, j + y))

bfs(adjacency_list, distance, used, (x1, y1))

dist = distance[x2][y2]
path = []
next = used[x2][y2]
for i in range(dist):
	path.append(next)
	next = used[next[0]][next[1]]
path.reverse()

print(dist + 1)
for step in path:
	print(' '.join([str(x + 1) for x in step]))
print(' '.join([str(x + 1) for x in (x2, y2)]))