from sys import stdin, stdout


class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.high = 1
		self.balance = 0
		self.sum = value
		self.left_bound = value
		self.right_bound = value


class Tree:

	DIS_BALANCE = 2
	MODE_VALUE = 10 ** 9

	def __init__(self):
		self.root = None
		self.last_response = 0

	def fix(self, node):
		left_high = 0 if node.left is None else node.left.high
		right_high = 0 if node.right is None else node.right.high
		node.high = max(left_high, right_high) + 1
		node.balance = left_high - right_high
		node.left_bound = node.value if node.left is None else node.left.left_bound
		node.right_bound = node.value if node.right is None else node.right.right_bound
		left_sum = 0 if node.left is None else node.left.sum
		right_sum = 0 if node.right is None else node.right.sum
		node.sum = left_sum + right_sum + node.value
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
		if node.balance == -self.DIS_BALANCE and node.right.balance <= 0:
			node = self.small_rotate_left(node)
		elif node.balance == -self.DIS_BALANCE and node.right.balance > 0:
			node = self.big_rotate_left(node)
		elif node.balance == self.DIS_BALANCE and node.left.balance >= 0:
			node = self.small_rotate_right(node)
		elif node.balance == self.DIS_BALANCE and node.left.balance < 0:
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


	def get_sum(self, node, left, right):
		curr_sum = 0
		if node is None:
			return 0
		if left <= node.left_bound and right >= node.right_bound:
			curr_sum += node.sum
		elif (right <= node.right_bound and right >= node.left_bound) or (left >= node.left_bound and left <= node.right_bound):
			curr_sum += self.get_sum(node.left, left, right)
			curr_sum += self.get_sum(node.right, left, right)
			if node.value >= left and node.value <= right:
				curr_sum += node.value
		return curr_sum


n = int(input())
tree = Tree()
for i in range(n):
	row = stdin.readline().split(' ')
	if row[0] == '+':
		new_value = (int(row[1]) + tree.last_response) % tree.MODE_VALUE
		tree.root = tree.insert(tree.root, new_value)
		tree.last_response = 0
	elif row[0] == '?':
		tree.last_response = tree.get_sum(tree.root, int(row[1]), int(row[2]))
		stdout.write(str(tree.last_response) + '\n')
