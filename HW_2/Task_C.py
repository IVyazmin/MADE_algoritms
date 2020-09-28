MAX_VALUE = ord('z') - ord('a') + 1
FIRST_VALUE = ord('a')

row = input()
array = row.split(' ')
array = list(map(int, array))
n = array[0]
m = array[1]
k = array[2]
array = []
for i in range(n):
	array.append(input())

for i in range(k):
	position = m - i - 1
	counters = [0] * MAX_VALUE
	new_array = [0] * n
	for j in range(n):
		element = array[j][position]
		counters[ord(element) - FIRST_VALUE] += 1
	pos_counters = [0] * MAX_VALUE
	for j in range(1, MAX_VALUE):
		pos_counters[j] = pos_counters[j - 1] + counters[j - 1]
	for j in range(n):
		element = array[j][position]
		elem_pos = pos_counters[ord(element) - FIRST_VALUE]
		new_array[elem_pos] = array[j]
		pos_counters[ord(element) - FIRST_VALUE] += 1
	array = new_array

for i in range(n):
	print(array[i])