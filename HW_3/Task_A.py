def bin_search(array, x):
	left = -1
	right = len(array)
	while right - left > 1:
		middle = (right + left) // 2
		if array[middle] == x:
			return x
		elif array[middle] < x:
			left = middle
		else:
			right = middle
			
	if left == -1:
		return array[0]
	if right == len(array):
		return array[-1]

	if x - array[left] <= array[right] - x:
		best_choice = array[left]
	else:
		best_choice = array[right]
	return best_choice


n, k = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
requestes = list(map(int, input().split(' ')))

for request in requestes:
	resp = bin_search(array, request)
	print(resp)