import math

A_CONST_1 = 23
A_CONST_2 = 21563
A_CONST_3 = 16714589
U_CONST_1 = 17
U_CONST_2 = 751
U_CONST_3 = 2
V_CONST_1 = 13
V_CONST_2 = 593
v_CONST_3 = 5

n, m, a_i = map(int, input().split(' '))
u, v = map(int, input().split(' '))

a_array = [0] * n
a_array[0] = a_i
for i in range(1, n):
	a_array[i] = (A_CONST_1 * a_array[i - 1] + A_CONST_2) % A_CONST_3

pre_sum = []
for i in range(n):
	pre_sum.append([])
	pre_sum[i].append(a_array[i])

i = 1
while i <= round(math.log2(n)):
	for j in range(n):
		if j + 2 ** i <= n:
			second_idx = int(j + 2 ** (i - 1))
			next = min(pre_sum[j][-1], pre_sum[second_idx][-1])
			pre_sum[j].append(next)
	i += 1

pow_array = [0] * (n + 1)
for i in range(2, n + 1):
	pow_array[i] = pow_array[i - 1]
	if 2 ** (pow_array[i] + 1) <= i:
		pow_array[i] += 1

i = 1
while True:
	start = min(u, v) - 1
	end = max(u, v) - 1
	max_pow = pow_array[end - start + 1]
	second_idx = end - 2 ** max_pow + 1
	result = min(pre_sum[start][max_pow], pre_sum[second_idx][max_pow])
	if i == m:
		break
	u = ((U_CONST_1 * u + U_CONST_2 + result + U_CONST_3 * i) % n) + 1
	v = ((V_CONST_1 * v + V_CONST_2 + result + v_CONST_3 * i) % n) + 1
	i += 1

print(' '.join([str(u), str(v), str(result)]))