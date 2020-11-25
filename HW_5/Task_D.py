from sys import stdin, stdout

class MySet:

	size = 300
	resize = 20
	rip = 1000000001
	hash_a = 1013
	hash_p = 1001


	def __init__(self):
		self.elements = [None] * MySet.size
		self.count_elements = 0
		self.cur_size = MySet.size


	def hash(self, value):
		result = 0
		cur_a = MySet.hash_a
		for char in value:
			result = (result * cur_a + ord(char)) % MySet.hash_p
			cur_a = cur_a * MySet.hash_a % MySet.hash_p
		return result % self.cur_size

	def rehash(self):
		# print(self.elements)
		self.cur_size = self.cur_size * MySet.resize
		new_elements = [None] * self.cur_size
		self.count_elements = 0
		for elem in self.elements:
			if elem is not None and elem != MySet.rip:
				hash_v = self.hash(elem)
				while new_elements[hash_v] is not None:
					hash_v = (hash_v + 1) % self.cur_size
				new_elements[hash_v] = elem
				self.count_elements += 1
		self.elements = new_elements
		# print(self.elements)
		# print(self.count_elements)

	def insert(self, value):
		hash_v = self.hash(value)
		while self.elements[hash_v] is not None and self.elements[hash_v] != MySet.rip:
			if self.elements[hash_v] == value:
				return
			hash_v = (hash_v + 1) % self.cur_size
		self.elements[hash_v] = value
		self.count_elements += 1
		if self.count_elements > self.cur_size // 2:
			#print(1)
			self.rehash()


	def delete(self, value):
		hash_v = self.hash(value)
		while self.elements[hash_v] is not None:
			if self.elements[hash_v] == value:
				self.elements[hash_v] = MySet.rip
				return
			hash_v = (hash_v + 1) % self.cur_size


	def get_list(self):
		count = 0
		real_elements = []
		for elem in self.elements:
			if elem is not None and elem != MySet.rip:
				real_elements.append(elem)
				count += 1
		real_elements = [str(count),] + real_elements
		return real_elements


class Node:
 
	def __init__(self, key, my_set, next):
		self.key = key
		self.set = my_set
		self.next = next
 
 
class LinkedList:
 
	def __init__(self):
		self.head = None
 
	def exists(self, key):
		current = self.head
		while current is not None:
			if current.key == key:
				return current
			current = current.next
		return None
 
	def insert(self, key, value):
		existed_node = self.exists(key)
		if existed_node is not None:
			existed_node.set.insert(value)
		else:
			my_set = MySet()
			my_set.insert(value)
			self.head = Node(key, my_set, self.head)
	
	def delete(self, key, value):
		if self.head is None:
			return
		current = self.head
		while current is not None:
			if current.key == key:
				current.set.delete(value)
				break
			current = current.next

	def delete_all(self, key):
		if self.head is None:
			return
		if self.head.key == key:
			self.head = self.head.next
			return
		prev = self.head
		current = self.head.next
		while current is not None:
			if current.key == key:
				prev.next = current.next
				break
			prev = current
			current = current.next
 
 
class MyMap:
 
	size = 400000
	hash_a = 10001
	hash_p = 1000001
 
	def __init__(self):
		self.elements = [None] * MyMap.size
 
	def hash(self, value):
		result = 0
		cur_a = MyMap.hash_a
		for char in value:
			result = (result * cur_a + ord(char)) % MyMap.hash_p
			cur_a = cur_a * MyMap.hash_a % MyMap.hash_p
		return result % MyMap.size
 
	def put(self, key, value):
		hash_v = self.hash(key)
		if self.elements[hash_v] is None:
			self.elements[hash_v] = LinkedList()
		self.elements[hash_v].insert(key, value)
 
	def get(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is None:
			result = ['0']
		else:
			element = self.elements[hash_v].exists(key)
			if element is None:
				result = ['0']
			else:
				result = element.set.get_list()
		return result
 
	def delete(self, key, value):
		hash_v = self.hash(key)
		if self.elements[hash_v] is not None:
			self.elements[hash_v].delete(key, value)

	def delete_all(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is not None:
			self.elements[hash_v].delete_all(key)
 
 
# my_map = MyMap()
# for row in stdin:
# 	row = row.split(' ')
# 	if row[0] == 'put':
# 		my_map.put(row[1], row[2].rstrip('\n'))
# 	elif row[0] == 'get':
# 		result = ' '.join(my_map.get(row[1].rstrip('\n'))) + '\n'
# 		stdout.buffer.write(result.encode())
# 	elif row[0] == 'delete':
# 		my_map.delete(row[1], row[2].rstrip('\n'))
# 	elif row[0] == 'deleteall':
# 		my_map.delete_all(row[1].rstrip('\n'))

my_map = MyMap()
for row in stdin:
	row = row.split(' ')
	if row[0] == 'put':
		my_map.put(row[1], row[2].rstrip('\n'))
	elif row[0] == 'get':
		result = ' '.join(my_map.get(row[1].rstrip('\n'))) + '\n'
		stdout.write(result)
	elif row[0] == 'delete':
		my_map.delete(row[1], row[2].rstrip('\n'))
	elif row[0] == 'deleteall':
		my_map.delete_all(row[1].rstrip('\n'))