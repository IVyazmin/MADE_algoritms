from sys import stdin, stdout
from math import log2, sqrt, ceil


def get_func(x):
	return x * x + sqrt(x)


def bin_search(x):
	ACCUR = 0.1 ** 6
	left = 0
	right = 1
	while c > right:
		right *= 2
	iter_count = ceil(log2((right - left) / ACCUR))

	for i in range(iter_count):
		middle = (right + left) / 2
		mid_value = get_func(middle)
		if mid_value < x:
			left = middle
		else:
			right = middle
	return right


c = float(stdin.readline())
stdout.write(str(bin_search(c)))