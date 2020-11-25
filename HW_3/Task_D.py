from sys import stdin, stdout


def get_count(array, x):
	counter = 0
	for value in array:
		counter += value // x
	return counter


def bin_search(array, k):
	left = 0
	right = array[-1] + 1
	while right - left > 1:
		middle = (right + left) // 2
		count = get_count(array, middle)
		if count >= k:
			left = middle
		else:
			right = middle
	return left


row = list(map(int, stdin.readline().split(' ')))
n = row[0]
k = row[1]
array = []
for i in range(n):
	array.append(int(stdin.readline()))
array = sorted(array)
stdout.write(str(bin_search(array, k)))