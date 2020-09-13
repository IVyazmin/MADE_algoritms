t = int(input())
for i in range(t):
	row = [int(x) for x in input().split(' ')]
	print(sum(row))