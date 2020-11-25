from sys import stdin, stdout
from random import randint


class Node:

	def __init__(self, value, prior):
		self.value = value
		self.prior = prior
		self.left = None
		self.right = None
		self.size = 1


class Tree:

	MAX_PRIOR = 10 ** 10

	def __init__(self):
		self.root = None

	def fix(self, node):
		left_size = 0 if node.left is None else node.left.size
		right_size = 0 if node.right is None else node.right.size
		node.size = left_size + right_size + 1
		return

	def split(self, node, x):
		if node is None:
			return None, None
		left_size = 0 if node.left is None else node.left.size
		if left_size > x:
			left, right = self.split(node.left, x)
			node.left = right
			self.fix(node)
			return left, node
		else:
			left, right = self.split(node.right, x - left_size - 1)
			node.right = left
			self.fix(node)
			return node, right

	def merge(self, left, right):
		if left is None:
			return right
		if right is None:
			return left
		if left.prior > right.prior:
			left.right = self.merge(left.right, right)
			self.fix(left)
			return left
		else:
			right.left = self.merge(left, right.left)
			self.fix(right)
			return right

	def insert(self, i, value, prior):
		new_node = Node(value, prior)
		left, right = self.split(self.root, i - 1)
		left = self.merge(left, new_node)
		root = self.merge(left, right)
		return root

	def delete(self, i):
		left, right = self.split(self.root, i - 1)
		left, _ = self.split(left, i - 2)
		root = self.merge(left, right)
		return root

	def get_array(self, node):
		if node is None:
			return []
		array = self.get_array(node.left)
		array.append(node.value)
		array += self.get_array(node.right)
		return array


n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
tree = Tree()
for i in range(n):
	tree.root = tree.insert(i + 1, array[i], randint(0, tree.MAX_PRIOR))

for i in range(m):
	row = stdin.readline().split(' ')
	if row[0] == 'add':
		tree.root = tree.insert(int(row[1]), int(row[2]), randint(0, tree.MAX_PRIOR))
	elif row[0] == 'del':
		tree.root = tree.delete(int(row[1]))

size = 0 if tree.root is None else tree.root.size
array = tree.get_array(tree.root)
array = ' '.join(map(str, array))
print(size)
print(array)
