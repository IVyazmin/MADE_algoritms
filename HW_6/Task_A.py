n, k = map(int, input().split(' '))
places = list(map(int, input().split(' '))) + [0]
money = [0]
way = [1]
for i in range(1, n):
	first = max(i - k, 0)
	best = first
	for j in range(first, i):
		if money[j] > money[best]:
			best = j
	way.append(best)
	money.append(money[best] + places[i - 1])

len_way = 0
best_way = [n]
while best_way[-1] != 1:
	best_way.append(way[best_way[-1] - 1] + 1)
	len_way += 1
best_way = map(str, best_way)
best_way = list(best_way)[::-1]

print(money[n - 1])
print(len_way)
print(' '.join(best_way))