from sys import stdin, stdout

class Node:

	def __init__(self, key, value, next, left):
		self.key = key
		self.value = value
		self.next = next
		self.left = left
		self.right = None


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

	def insert(self, key, value, left):
		existed_node = self.exists(key)
		if existed_node is not None:
			existed_node.value = value
			return left
		else:
			self.head = Node(key, value, self.head, left)
			if left is not None:
				self.head.left.right = self.head
			return self.head
	
	def delete(self, key):
		if self.head is None:
			return
		if self.head.key == key:
			if self.head.left is not None:
				self.head.left.right = self.head.right
			if self.head.right is not None:
				self.head.right.left = self.head.left
			self.head = self.head.next
			return
		prev = self.head
		current = self.head.next
		while current is not None:
			if current.key == key:
				prev.next = current.next
				if current.left is not None:
					current.left.right = current.right
				if current.right is not None:
					current.right.left = current.left
				break
			prev = current
			current = current.next


class MyMap:

	SIZE = 200000
	HASH_A = 10001
	HASH_P = 600001

	def __init__(self):
		self.elements = [None] * MyMap.SIZE
		self.last = None

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
		self.last = self.elements[hash_v].insert(key, value, self.last)

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

	def prev(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is None:
			result = 'none'
		else:
			element = self.elements[hash_v].exists(key)
			if element is None or element.left is None:
				result = 'none'
			else:
				result = element.left.value
		return result

	def next(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is None:
			result = 'none'
		else:
			element = self.elements[hash_v].exists(key)
			if element is None or element.right is None:
				result = 'none'
			else:
				result = element.right.value
		return result

	def delete(self, key):
		hash_v = self.hash(key)
		if self.elements[hash_v] is not None:
			self.elements[hash_v].delete(key)
		if self.last is not None and key == self.last.key:
			self.last = self.last.left


my_map = MyMap()
for row in stdin:
	row = row.split(' ')
	if row[0] == 'put':
		my_map.put(row[1], row[2].rstrip('\n'))
	elif row[0] == 'get':
		stdout.write(my_map.get(row[1].rstrip('\n')) + '\n')
	elif row[0] == 'delete':
		my_map.delete(row[1].rstrip('\n'))
	elif row[0] == 'prev':
		stdout.write(my_map.prev(row[1].rstrip('\n')) + '\n')
	elif row[0] == 'next':
		stdout.write(my_map.next(row[1].rstrip('\n')) + '\n')
