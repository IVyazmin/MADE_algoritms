def less(a, b):
	if a[0][:a[1]] < b[0][:b[1]]:
		return True
	elif (a[0][:a[1]] == b[0][:b[1]]) and (a[2] < b[2]):
		return True
	return False

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
	middle = len(array) // 2
	left = sort(array[:middle])
	right = sort(array[middle:])
	return merge(left, right)

def get_number(rom_num):
	dozens = 0
	ones = 0

	if rom_num == 'L':
		dozens = 5
		rom_num = ''
	elif rom_num[:2] == 'XL':
		dozens = 4
		rom_num = rom_num[2:]
	elif rom_num[-2:] == 'IX':
		dozens = rom_num.count('X') - 1
		rom_num = rom_num[dozens:]
	else:
		dozens = rom_num.count('X')
		rom_num = rom_num[dozens:]

	pos_5 = rom_num.find('V')
	if len(rom_num) == 0:
		ones = 0
	elif rom_num[-1] == 'X':
		ones = 9
	elif pos_5 == -1:
		ones = len(rom_num)
	elif pos_5 == 1:
		ones = 4
	else:
		ones = 4 + len(rom_num)

	return dozens * 10 + ones

array = list()
n = int(input())
for i in range(n):
	row = [0, 0, 0]
	row[0] = input()
	row[1] = row[0].find(' ')
	row[2] = get_number(row[0][row[1] + 1 :])
	array.append(row)
sorted_array = sort(array)
for i in range(n):
	print(sorted_array[i][0])