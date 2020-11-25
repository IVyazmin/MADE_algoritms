from sys import stdin, stdout


class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class Tree:

	def __init__(self):
		self.root = None

	def exists(self, node, value):
		if node is None:
			result = 'false'
		elif node.value == value:
			result = 'true'
		elif node.value > value:
			result = self.exists(node.left, value)
		elif node.value < value:
			result = self.exists(node.right, value)
		return result

	def prev(self, value):
		prev = None
		cur = self.root
		while cur is not None:
			if cur.value >= value:
				cur = cur.left
			else:
				prev = cur
				cur = cur.right
		if prev is None:
			result = 'none'
		else:
			result = str(prev.value)
		return result

	def next(self, value):
		next = None
		cur = self.root
		while cur is not None:
			if cur.value <= value:
				cur = cur.right
			else:
				next = cur
				cur = cur.left
		if next is None:
			result = 'none'
		else:
			result = str(next.value)
		return result

	def insert(self, node, value):
		if node is None:
			node = Node(value)
		elif node.value > value:
			node.left = self.insert(node.left, value)
		elif node.value < value:
			node.right = self.insert(node.right, value)
		return node

	def get_max(self, node):
		while node.right is not None:
			node = node.right
		return node.value

	def delete(self, node, value):
		if node is None:
			return None
		if node.value > value:
			node.left = self.delete(node.left, value)
		elif node.value < value:
			node.right = self.delete(node.right, value)
		elif node.value == value:
			if node.left is None:
				node = node.right
			else:
				node.value = self.get_max(node.left)
				node.left = self.delete(node.left, node.value)
		return node

tree = Tree()
for row in stdin:
	row = row.split(' ')
	if row[0] == 'insert':
		tree.root = tree.insert(tree.root, int(row[1]))
	elif row[0] == 'delete':
		tree.root = tree.delete(tree.root, int(row[1]))
	if row[0] == 'exists':
		stdout.write(str(tree.exists(tree.root, int(row[1]))) + '\n')
	if row[0] == 'prev':
		stdout.write(tree.prev(int(row[1])) + '\n')
	if row[0] == 'next':
		stdout.write(tree.next(int(row[1])) + '\n')