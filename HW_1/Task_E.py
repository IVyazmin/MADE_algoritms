def split(array, mean):
	p1 = -1
	count_mid = 0
	for i in range(0, len(array)):
		if array[i] < mean:
			array[p1 + 1], array[i] = array[i], array[p1 + 1]
			if count_mid > 0:
				array[p1 + count_mid + 1], array[i] = array[i], array[p1 + count_mid + 1]
			p1 += 1
		elif array[i] == mean:
			array[p1 + count_mid + 1], array[i] = array[i], array[p1 + count_mid + 1]
			count_mid += 1
	return array[:p1 + 1], array[p1 + 1:p1 + count_mid + 1], array[p1 + count_mid + 1:]

def sort(array):
	if len(array) < 2:
		return array
	mean = (array[0] + array[-1]) / 2
	left, mid, right = split(array, mean)
	left = sort(left)
	right = sort(right)
	return left + mid + right
n = int(input())
array = list(map(int, input().split(' ')))
array = sort(array)
array = list(map(str, array))
row = ' '.join(array)
print(row)