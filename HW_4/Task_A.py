from sys import stdin, stdout

class Node:

	def __init__(self, value, next, cur_min):
		self.value = value
		self.next = next
		self.cur_min = cur_min


class Stack:

	def __init__(self):
		self.head = None
		self.size = 0

	def push(self, value):
		if self.size == 0:
			cur_min = value
		else:
			cur_min = min(value, self.head.cur_min)
		self.head = Node(value, self.head, cur_min)
		self.size += 1
	
	def pop(self):
		self.head = self.head.next
		self.size -= 1

	def get_min(self):
		return self.head.cur_min

stack = Stack()
n = int(stdin.readline())
for i in range(n):
	task = stdin.readline()
	comand = task[0]
	if comand == '1':
		stack.push(int(task[2:]))
	elif comand == '2':
		stack.pop()
	elif comand == '3':
		stdout.write(str(stack.get_min()) + '\n')
	