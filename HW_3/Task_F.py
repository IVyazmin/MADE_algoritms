from sys import stdin, stdout
from math import ceil, sqrt, log2

ACCUR = 0.1 ** 5

def get_func(v_field, v_forest, a, x):
	time = 0
	time += sqrt((1 - a) ** 2 + x ** 2) / v_field
	time += sqrt(a ** 2 + (1 - x) ** 2) / v_forest
	return time


def tern_search(v_field, v_forest, a):
	left = 0.0
	right = 1.0
	iter_count = ceil(log2((right - left) / ACCUR))
	for i in range(iter_count):
		point1 = (left + right) / 2 - ACCUR
		point2 = (left + right) / 2 + ACCUR
		time1 = get_func(v_field, v_forest, a, point1)
		time2 = get_func(v_field, v_forest, a, point2)
		if time1 < time2:
			right = point2
		else:
			left = point1
	return left


row = list(map(int, stdin.readline().split(' ')))
v_field = row[0]
v_forest = row[1]
a = float(stdin.readline())
stdout.write(str(tern_search(v_field, v_forest, a)))