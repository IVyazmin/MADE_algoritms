def less(a, b):
	if a[0][:a[1]] < b[0][:b[1]]:
		return True
	elif (a[0][:a[1]] == b[0][:b[1]]) and (a[2] < b[2]):
		return True
	return False

def merge(left, right):
	i = j = 0
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
		if less(left[i], right[j]):
			new_array.append(left[i])
			i += 1
		else:
			new_array.append(right[j])
			j += 1
	return new_array

def sort(array):
	if len(array) < 2:
		return array
	left = sort(array[:(len(array) // 2)])
	right = sort(array[(len(array) // 2):])
	return merge(left, right)

def get_number(string):
	number = 0
	i = 0
	if string == 'L':
		return 50
	while i < len(string) and string[i] == 'X':
		number += 10
		i += 1
	string = string[i:]
	if len(string) == 0:
		return number
	if string == 'L':
		return 40
	if string[0] == 'L':
		number = 40
		string = string[1:]
	if string[-1] == 'X':
		return number + 9
	pos_5 = string.find('V')
	if pos_5 == -1:
		return number + len(string)
	if pos_5 == 1:
		return number + 4
	return number + 5 + len(string) - 1

array = list()
n = int(input())
for i in range(n):
	row = [0] * 3
	row[0] = input()
	row[1] = row[0].find(' ')
	row[2] = get_number(row[0][row[1] + 1:])
	array.append(row)
sorted_array = sort(array)
for i in range(n):
	print(sorted_array[i][0])