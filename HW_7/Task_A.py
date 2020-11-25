POW_2_16 = 2 ** 16
POW_2_30 = 2 ** 30

n, x, y, a_0 = map(int, input().split(' '))
m, z, t, b_0 = map(int, input().split(' '))

pre_sum = [0] * n
pre_sum[0] = a_0
a_next = a_0
for i in range(1, n):
	a_next = (x * a_next + y) % POW_2_16
	pre_sum[i] = pre_sum[i - 1] + a_next

b_first = b_0
b_second = (z * b_first + t) % POW_2_30

total_sum = 0
for i in range(m):
	c_first = b_first % n
	c_second = b_second % n
	left = min(c_first, c_second)
	right = max(c_first, c_second)
	total_sum += pre_sum[right]
	if left > 0:
		total_sum -= pre_sum[left - 1]
	b_first = (z * b_second + t) % POW_2_30
	b_second = (z * b_first + t) % POW_2_30

print(total_sum)