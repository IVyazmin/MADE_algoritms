from sys import stdin, stdout

def lower_bound(array, x):
	left = -1
	right = len(array)
	while right - left > 1:
		middle = (right + left) // 2
		if array[middle] < x:
			left = middle
		else:
			right = middle
	return right


n = int(stdin.readline())
array = list(map(int, stdin.readline().split(' ')))
array = sorted(array)
k = int(stdin.readline())

answ = []
for i in range(k):
	row = list(map(int, stdin.readline().split(' ')))
	left = row[0]
	right = row[1]
	lb = lower_bound(array, left)
	ub = lower_bound(array, right + 1)
	answ.append(ub - lb)
answ = list(map(str, answ))
row = ' '.join(answ)
stdout.write(row)