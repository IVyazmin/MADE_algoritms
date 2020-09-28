row = input()
array = row.split(' ')
array = map(int, array)
MAX_VALUE = 101
counters = [0] * MAX_VALUE
for number in array:
	counters[number] += 1
new_array = []
for i, counter in enumerate(counters):
	new_array += [i] * counter
new_array = map(str, new_array)
row = ' '.join(new_array)
print(row)