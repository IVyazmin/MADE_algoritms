n = int(input())
numbers = list(map(int, input().split(' ')))
lengths = [0] * n
positions = [-1] * n

for i in range(n):
	for j in range(i):
		if numbers[j] < numbers[i] and lengths[j] > lengths[i]:
			lengths[i] = lengths[j]
			positions[i] = j
	lengths[i] += 1

max_len = 0
best_seq = []
next = -1
for i in range(n):
	if lengths[i] > max_len:
		max_len = lengths[i]
		next = i

while next != -1:
	best_seq.append(numbers[next])
	next = positions[next]
best_seq.reverse()
best_seq = map(str, best_seq)
best_seq = ' '.join(best_seq)

print(max_len)
print(best_seq)