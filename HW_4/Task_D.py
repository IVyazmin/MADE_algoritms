from sys import stdin, stdout

class Pair:

	def __init__(self, value, row_number):
		self.value = value
		self.row_number = row_number

class Heap:

	def __init__(self):
		self.elements = []
		self.size = 0
		self.comands = []
		self.len_comands = 0

	def swap(self, i, j):
		self.elements[i], self.elements[j] = self.elements[j], self.elements[i]
		comands_i = self.elements[i].row_number
		comands_j = self.elements[j].row_number
		self.comands[comands_i], self.comands[comands_j] = self.comands[comands_j], self.comands[comands_i]

	def push(self, value, row_number):
		cur_index = self.size
		self.size += 1
		self.elements.append(Pair(value, row_number))
		self.comands += [0] * (row_number - self.len_comands) + [cur_index]
		self.len_comands = row_number + 1
		while cur_index > 0:
			if self.elements[(cur_index - 1) // 2].value > self.elements[cur_index].value:
				self.swap((cur_index - 1) // 2, cur_index)
				cur_index = (cur_index - 1) // 2
			else:
				break
		return

	def pop(self):
		if self.size == 0:
			return '*'
		element = (self.elements[0].value, self.elements[0].row_number + 1)
		self.swap(self.size - 1, 0)
		self.size -= 1
		self.comands[self.elements[self.size].row_number] = '*'
		self.elements = self.elements[:self.size]
		cur_index = 0
		while cur_index * 2 + 1 < self.size:
			if cur_index * 2 + 2 == self.size:
				if self.elements[cur_index].value > self.elements[cur_index * 2 + 1].value:
					self.swap(cur_index, cur_index * 2 + 1)
					cur_index = cur_index * 2 + 1
				else:
					break
			else:
				min_elem = min(self.elements[cur_index].value, self.elements[cur_index * 2 + 1].value, self.elements[cur_index * 2 + 2].value)
				if self.elements[cur_index * 2 + 1].value == min_elem:
					self.swap(cur_index, cur_index * 2 + 1)
					cur_index = cur_index * 2 + 1
				elif self.elements[cur_index * 2 + 2].value == min_elem:
					self.swap(cur_index, cur_index * 2 + 2)
					cur_index = cur_index * 2 + 2
				else:
					break
		return element

	def decrease(self, key, value):
		cur_index = self.comands[key]
		if cur_index == '*':
			return
		else:
			self.elements[cur_index].value = value
		self.elements[cur_index]
		while cur_index > 0:
			if self.elements[(cur_index - 1) // 2].value > self.elements[cur_index].value:
				self.swap((cur_index - 1) // 2, cur_index)
				cur_index = (cur_index - 1) // 2
			else:
				break
		return

heap = Heap()
row_number = 0
for row in stdin:
	row = row.split(' ')
	if row[0][:4] == 'push':
		heap.push(int(row[1]), row_number)
	elif row[0][:11] == 'extract-min':
		result = ' '.join(map(str, heap.pop()))
		stdout.write(result + '\n')
	elif row[0][:12] == 'decrease-key':
		heap.decrease(int(row[1]) - 1, int(row[2]))
	row_number += 1