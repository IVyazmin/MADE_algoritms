from sys import stdin, stdout

class Queue:

	standart_capacity = 4
	k_resize = 2

	def __init__(self):
		self.elements = [0] * Queue.standart_capacity
		self.head = 0
		self.tail = 0
		self.capacity = Queue.standart_capacity

	def get_size(self):
		if self.tail >= self.head:
			size = self.tail - self.head
		else:
			size = self.capacity + self.tail - self.head
		return size

	def add_memory(self):
		new_elements = [0] * (self.capacity * Queue.k_resize)
		for i in range(self.get_size()):
			new_elements[i] = self.elements[(i + self.head) % self.capacity]
		self.elements = new_elements
		self.tail = self.get_size()
		self.head = 0
		self.capacity = self.capacity * Queue.k_resize

	def decrease_memory(self):
		new_elements = [0] * (self.capacity // Queue.k_resize)
		for i in range(self.get_size()):
			new_elements[i] = self.elements[(i + self.head) % self.capacity]
		self.elements = new_elements
		self.tail = self.get_size()
		self.head = 0
		self.capacity = self.capacity // Queue.k_resize

	def push(self, value):
		if self.get_size() == self.capacity - 1:
			self.add_memory()
		self.elements[self.tail] = value
		self.tail = (self.tail + 1) % self.capacity

	def pop(self):
		element = self.elements[self.head]
		self.head = (self.head + 1) % self.capacity
		if self.get_size() <= self.capacity // (Queue.k_resize) ** 2:
			self.decrease_memory()
		return element

queue = Queue()
n = int(stdin.readline())
for i in range(n):
	row = stdin.readline()
	if row[0] == '+':
		queue.push(int(row[2:]))
	elif row[0] == '-':
		stdout.write(str(queue.pop()) + '\n')