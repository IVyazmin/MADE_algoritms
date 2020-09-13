n = int(input())
array = list(map(int, input().split(' ')))
for i in range(1, n):
	j = i
	while (j != 0) and (array[j] < array[j - 1]):
		array[j], array[j - 1] = array[j - 1], array[j]
		j -= 1
array = map(str, array)
print(' '.join(array))