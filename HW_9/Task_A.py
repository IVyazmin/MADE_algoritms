from sys import stdin, stdout
from random import randint


class Node:

	def __init__(self, value, prior):
		self.value = value
		self.prior = prior
		self.left = None
		self.right = None


class Tree:

	MAX_PRIOR = 10 ** 7

	def __init__(self):
		self.root = None

	def split(self, node, x):
		if node is None:
			return None, None
		if node.value > x:
			left, right = self.split(node.left, x)
			node.left = right
			return left, node
		else:
			left, right = self.split(node.right, x)
			node.right = left
			return node, right

	def merge(self, left, right):
		if left is None:
			return right
		if right is None:
			return left
		if left.prior > right.prior:
			left.right = self.merge(left.right, right)
			return left
		else:
			right.left = self.merge(left, right.left)
			return right

	def exists(self, node, value):
		if node is None:
			result = 'false'
		elif node.value == value:
			result = 'true'
		elif node.value > value:
			result = self.exists(node.left, value)
		else:
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

	def insert(self, node, value, prior):
		if node is  None:
			node = Node(value, prior)
		elif node.prior <= prior:
			if self.exists(node, value) != 'true':
				left, right = self.split(node, value)
				node = Node(value, prior)
				node.left = left
				node.right = right
		elif node.value > value:
			node.left = self.insert(node.left, value, prior)
		elif node.value < value:
			node.right = self.insert(node.right, value, prior)
		return node

	def delete(self, node, value):
		if node is None:
			return None
		if node.value > value:
			node.left = self.delete(node.left, value)
		elif node.value < value:
			node.right = self.delete(node.right, value)
		elif node.value == value:
			node = self.merge(node.left, node.right)
		return node


tree = Tree()
for row in stdin:
	row = row.split(' ')
	if row[0] == 'insert':
		tree.root = tree.insert(tree.root, int(row[1]), randint(0, tree.MAX_PRIOR))
	elif row[0] == 'delete':
		tree.root = tree.delete(tree.root, int(row[1]))
	if row[0] == 'exists':
		stdout.write(str(tree.exists(tree.root, int(row[1]))) + '\n')
	if row[0] == 'prev':
		stdout.write(tree.prev(int(row[1])) + '\n')
	if row[0] == 'next':
		stdout.write(tree.next(int(row[1])) + '\n')
		