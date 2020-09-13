def merge(left, right):
	i = j = 0
	len_l = len(left)
	len_r = len(right)
	new_array = []
	counter = 0
	while i + j < len_l + len_r:
		if i == len_l:
			new_array.append(right[j])
			j += 1
			continue
		if j == len_r:
			new_array.append(left[i])
			i += 1
			continue
		if left[i] <= right[j]:
			new_array.append(left[i])
			i += 1
		else:
			new_array.append(right[j])
			j += 1
			counter += (len_l - i)
	return new_array, counter

def sort(array):

	if len(array) < 2:
		return array, 0
	left, counter_l = sort(array[:(len(array) // 2)])
	right, counter_r = sort(array[(len(array) // 2):])
	array, counter_add = merge(left, right)
	return array, counter_l + counter_r + counter_add

n = int(input())
array = list(map(int, input().split(' ')))
counter = 0
_, counter = sort(array)
print(counter)