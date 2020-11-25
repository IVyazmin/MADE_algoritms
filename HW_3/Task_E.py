from sys import stdin, stdout


def get_count(time, x, y):
	if time < min(x, y):
		return 0
	counter = 1
	time -= min(x, y)
	counter += time // x
	counter += time // y
	return counter


def bin_search(n, x, y):
	left = 0
	right = n * min(x, y)
	while right - left > 1:
		middle = (right + left) // 2
		count = get_count(middle, x, y)
		if count >= n:
			right = middle
		else:
			left = middle
	return right


row = list(map(int, stdin.readline().split(' ')))
n = row[0]
x = row[1]
y = row[2]
stdout.write(str(bin_search(n, x, y)))