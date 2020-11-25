from sys import stdin, stdout

class MySet:

	SIZE = 2000000
	RIP = 1000000001
	HASH_A = 1001
	HASH_P = 10000001


	def __init__(self):
		self.elements = [None] * MySet.SIZE


	def hash(self, value):
		return (value * MySet.HASH_A) % MySet.HASH_P % MySet.SIZE


	def insert(self, value):
		hash_v = self.hash(value)
		while self.elements[hash_v] is not None and self.elements[hash_v] != MySet.RIP:
			if self.elements[hash_v] == value:
				return
			hash_v = (hash_v + 1) % MySet.SIZE
		self.elements[hash_v] = value


	def exists(self, value):
		hash_v = self.hash(value)
		while self.elements[hash_v] is not None:
			if self.elements[hash_v] == value:
				return 'true'
			hash_v = (hash_v + 1) % MySet.SIZE
		return 'false'

	def delete(self, value):
		hash_v = self.hash(value)
		while self.elements[hash_v] is not None:
			if self.elements[hash_v] == value:
				self.elements[hash_v] = MySet.RIP
				return
			hash_v = (hash_v + 1) % MySet.SIZE

my_set = MySet()
for row in stdin.buffer:
	row = row.decode('utf8').split(' ')
	if row[0] == 'insert':
		my_set.insert(int(row[1]))
	elif row[0] == 'exists':
		result = my_set.exists(int(row[1])) + '\n'
		stdout.buffer.write(result.encode())
	elif row[0] == 'delete':
		my_set.delete(int(row[1]))