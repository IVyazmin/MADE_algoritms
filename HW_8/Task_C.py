from sys import stdin, stdout


class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.high = 1
		self.balance = 0
		self.count = 1


class Tree:

	def __init__(self):
		self.root = None

	def fix(self, node):
		left_high = 0 if node.left is None else node.left.high
		right_high = 0 if node.right is None else node.right.high
		left_count = 0 if node.left is None else node.left.count
		right_count = 0 if node.right is None else node.right.count
		node.high = max(left_high, right_high) + 1
		node.count = left_count + right_count + 1
		node.balance = left_high - right_high
		return

	def small_rotate_left(self, node):
		new_root = node.right
		node.right = new_root.left
		new_root.left = node
		self.fix(node)
		self.fix(new_root)
		return new_root

	def small_rotate_right(self, node):
		new_root = node.left
		node.left = new_root.right
		new_root.right = node
		self.fix(node)
		self.fix(new_root)
		return new_root

	def big_rotate_left(self, node):
		node.right = self.small_rotate_right(node.right)
		return self.small_rotate_left(node)

	def big_rotate_right(self, node):
		node.left = self.small_rotate_left(node.left)
		return self.small_rotate_right(node)

	def balance(self, node):
		if node is None:
			return node
		if node.balance == -2 and node.right.balance <= 0:
			node = self.small_rotate_left(node)
		elif node.balance == -2 and node.right.balance > 0:
			node = self.big_rotate_left(node)
		elif node.balance == 2 and node.left.balance >= 0:
			node = self.small_rotate_right(node)
		elif node.balance == 2 and node.left.balance < 0:
			node = self.big_rotate_right(node)
		return node

	def insert(self, node, value):
		if node is None:
			node = Node(value)
		elif node.value > value:
			node.left = self.insert(node.left, value)
		elif node.value < value:
			node.right = self.insert(node.right, value)
		self.fix(node)
		return self.balance(node)

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
		if node is not None:
			self.fix(node)
		return self.balance(node)

	def get_k_max(self, node, k):
		number = node.count - k + 1
		left_count = 0 if node.left is None else node.left.count
		right_count = node.count - left_count - 1
		if number == left_count + 1:
			result = node.value
		elif number <= left_count:
			result = self.get_k_max(node.left, k - right_count - 1)
		else:
			result = self.get_k_max(node.right, k)
		return result

	def print_tree(self, node):
		if node is not None:
			self.print_tree(node.left)
			print(node.value)
			self.print_tree(node.right)


n = int(input())
tree = Tree()
for i in range(n):
	row = stdin.readline().split(' ')
	if row[0] == '+1' or row[0] == '1':
		tree.root = tree.insert(tree.root, int(row[1]))
	elif row[0] == '-1':
		tree.root = tree.delete(tree.root, int(row[1]))
	elif row[0] == '0':
		stdout.write(str(tree.get_k_max(tree.root, int(row[1]))) + '\n')
