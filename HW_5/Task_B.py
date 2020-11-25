from sys import stdin, stdout
 
class Node:
 
	def __init__(self, key, value, next):
		self.key = key
		self.value = value
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
			existed_node.value = value
		else:
			self.head = Node(key, value, self.head)
	
	def delete(self, key):
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
 
	SIZE = 200000
	HASH_A = 10001
	HASH_P = 1000001
 
	def __init__(self):
		self.elements = [None] * MyMap.SIZE
 
	def hash(self, value):
		result = 0
		cur_a = MyMap.HASH_A
		for char in value:
			result = (result * cur_a + ord(char)) % MyMap.HASH_P
			cur_a = cur_a * MyMap.HASH_A % MyMap.HASH_P
		return result % MyMap.SIZE
 
	def put(self, key, value):
		hash_v = self.hash(key)
		if self.elements[hash_v] is None:
			self.elements[hash_v] = LinkedList()
		self.elements[hash_v].insert(key, value)
 
	def get(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is None:
			result = 'none'
		else:
			element = self.elements[hash_v].exists(key)
			if element is None:
				result = 'none'
			else:
				result = element.value
		return result
 
	def delete(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is not None:
			self.elements[hash_v].delete(key)
 
 
my_map = MyMap()
for row in stdin:
	row = row.split(' ')
	if row[0] == 'put':
		my_map.put(row[1], row[2].rstrip('\n'))
	elif row[0] == 'get':
		stdout.write(my_map.get(row[1].rstrip('\n')) + '\n')
	elif row[0] == 'delete':
		my_map.delete(row[1].rstrip('\n'))