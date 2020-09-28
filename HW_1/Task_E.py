def split(array, left, right, mean):
	pvt = left
	count_mid = 0
	for i in range(left, right):
		swap_idx = pvt + count_mid
		if array[i] < mean:
			array[pvt], array[i] = array[i], array[pvt]
			if count_mid > 0:
				array[swap_idx], array[i] = array[i], array[swap_idx]
			pvt += 1
		elif array[i] == mean:
			array[swap_idx], array[i] = array[i], array[swap_idx]
			count_mid += 1
	return pvt, pvt + count_mid

def sort(array, left, right):
	if right - left < 2:
		return
	mean = (array[left] + array[right - 1]) / 2
	pvt1, pvt2 = split(array, left, right, mean)
	sort(array, left, pvt1)
	sort(array, pvt2, right)
	return
	
n = int(input())
array = list(map(int, input().split(' ')))
sort(array, 0, n)
array = list(map(str, array))
row = ' '.join(array)
print(row)