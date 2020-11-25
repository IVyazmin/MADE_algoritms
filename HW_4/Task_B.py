class Array:

	standart_capacity = 2
	k_resize = 2

	def __init__(self):
		self.elments = [0] * Array.standart_capacity
		self.size = 0
		self.capacity = Array.standart_capacity

	def add_memory(self):
		self.capacity = self.capacity * Array.k_resize
		new_elements = [0] * (self.capacity)
		for i in range(self.size):
			new_elements[i] = self.elments[i]
		self.elments = new_elements
		

	def decrease_memory(self):
		self.capacity = self.capacity // Array.k_resize
		new_elements = [0] * (self.capacity)
		for i in range(self.size):
			new_elements[i] = self.elments[i]
		self.elments = new_elements
		

	def push(self, value):
		if self.size == self.capacity:
			self.add_memory()
		self.elments[self.size] = value
		self.size += 1

	def pop(self):
		element = self.elments[self.size - 1]
		self.size -= 1
		if self.size <= self.capacity // (Array.k_resize) ** 2:
			self.decrease_memory()
		return element

array = Array()
row = input().split(' ')
comands = ('+', '-', '*')
for elem in row:
	if elem not in comands:
		array.push(int(elem))
	else:
		number2 = array.pop()
		number1 = array.pop()
		if elem == '+':
			result = number1 + number2
		elif elem == '-':
			result = number1 - number2
		elif elem == '*':
			result = number1 * number2
		array.push(result)
print(array.pop())