from sys import stdin, stdout

class Fenv_tree:

	def __init__(self, len_a, array):
		self.len_a = len_a
		self.array = array
		self.pre_sum = [0] * len_a
		for i in range(len_a):
			f_idx = i & (i + 1)
			self.pre_sum[i] = sum(self.array[f_idx : i + 1])

	def get_pre_sum(self, i):
		result = 0
		while i >= 0:
			result += self.pre_sum[i]
			i = (i & (i + 1)) - 1
		return result

	def get_sum(self, left, right):
		if left == 0:
			result = self.get_pre_sum(right)
		else:
			result = self.get_pre_sum(right) - self.get_pre_sum(left - 1)
		return result

	def set_elem(self, idx, elem):
		delta = elem - self.array[idx]
		self.array[idx] = elem
		i = idx
		while i < n:
			self.pre_sum[i] += delta
			i = i | (i + 1)
		return


n = int(input())
array = list(map(int, input().split(' ')))
tree = Fenv_tree(n, array)

for row in stdin:
	row = row.split(' ')
	if row[0] == 'sum':
		result = tree.get_sum(int(row[1]) - 1, int(row[2]) - 1)
		stdout.write(str(result) + '\n')
	elif row[0] == 'set':
		tree.set_elem(int(row[1]) - 1, int(row[2]))