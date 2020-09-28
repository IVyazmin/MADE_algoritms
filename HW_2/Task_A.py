from random import randint

def split(array, mean):
	p1 = -1
	count_mid = 0
	for i in range(0, len(array)):
		swap_idx = p1 + count_mid + 1
		if array[i] < mean:
			array[p1 + 1], array[i] = array[i], array[p1 + 1]
			if count_mid > 0:
				array[swap_idx], array[i] = array[i], array[swap_idx]
			p1 += 1
		elif array[i] == mean:
			array[swap_idx], array[i] = array[i], array[swap_idx]
			count_mid += 1
	less_idx = p1 + 1
	more_idx = p1 + count_mid + 1
	print(less_idx, more_idx)
	return less_idx, more_idx

def get_mean(max_idx, array):
	idxes = [0] * 3
	idxes[0] = 0
	idxes[1] = max_idx
	idxes[2] = max_idx // 2

	if array[idxes[0]] <= array[idxes[1]] and array[idxes[0]] <= array[idxes[2]]:
		if array[idxes[1]] < array[idxes[2]]:
			return idxes[1]
		else:
			return idxes[2]
	if array[idxes[1]] <= array[idxes[2]]:
		if array[idxes[0]] < array[idxes[2]]:
			return idxes[0]
		else:
			return idxes[2]
	if array[idxes[0]] < array[idxes[1]]:
		return idxes[0]
	else:
		return idxes[1]

def statisic(array, i, j, k):
	print(array[i:j], k)
	if len(array[i:j]) < 2:
		return array[i]
	
	#mean_ind = get_mean(len(array) - 1, array)
	#mean_ind = randint(0, len(array) - 1)
	#mean = array[mean_ind]
	#left, mid, right = split(array[i:j], mean)
	if (i, j) in hist.keys():
		less_idx, more_idx = hist[(i, j)]
	else:
		mean = (array[i] + array[j - 1]) / 2
		less_idx, more_idx = split(array[i:j], mean)
		less_idx += i
		more_idx += i
		hist[(i, j)] = (less_idx, more_idx)
	if k <= less_idx:
		k_stat = statisic(array, i, less_idx, k)
	elif k <= more_idx:
		k_stat = array[less_idx]
	else:
		k_stat = statisic(array, more_idx, j, k)
	return k_stat
	
n = int(input())
array = list(map(int, input().split(' ')))
m = int(input())
hist = dict()
for i in range(m):
	row = list(map(int, input().split(' ')))
	k_stat = statisic(array, row[0] - 1, row[1], row[2])
	print(k_stat)