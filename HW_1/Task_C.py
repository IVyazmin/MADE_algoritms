def merge(left, right):
	i = 0
	j = 0
	len_l = len(left)
	len_r = len(right)
	new_array = []
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
	return new_array

def sort(array):
	if len(array) < 2:
		return array
	middle = len(array) // 2
	left = sort(array[:middle])
	right = sort(array[middle:])
	return merge(left, right)

n = int(input())
array = list(map(int, input().split(' ')))
array = sort(array)
array = list(map(str, array))
row = ' '.join(array)
print(row)