MAX_VALUE = ord('z') - ord('a') + 1
FIRST_VALUE = ord('a')

def substr(cnt_s, cnt_t):
	for i in range(MAX_VALUE):
		if cnt_t[i] < cnt_s[i]:
			return False
	return True

row = input()
array = row.split(' ')
array = list(map(int, array))
n = array[0]
m = array[1]
s = input()
t = input()

counter_t = [0] * MAX_VALUE
counter_s = [0] * MAX_VALUE
counter_sub = 0

for i in range(m):
	counter_t[ord(t[i]) - FIRST_VALUE] += 1
for i in range(min(m, n)):
	counter_s[ord(s[i]) - FIRST_VALUE] += 1
counter_s_copy = counter_s[:]

for i in range(n - m):
	length_w = m
	while length_w > 0:
		if substr(counter_s, counter_t):
			break
		last = length_w + i - 1
		counter_s[ord(s[last]) - FIRST_VALUE] -= 1
		length_w -= 1
	counter_sub += length_w
	counter_s_copy[ord(s[i]) - FIRST_VALUE] -= 1
	counter_s_copy[ord(s[i + m]) - FIRST_VALUE] += 1
	counter_s = counter_s_copy[:]

tail = min(m, n)
for i in range(tail):
	length_w = tail - i
	while length_w > 0:
		if substr(counter_s, counter_t):
			break
		last = n - (tail - length_w - i + 1)
		counter_s[ord(s[last]) - FIRST_VALUE] -= 1
		length_w -= 1
	counter_sub += length_w
	ejected = n - tail + i
	counter_s_copy[ord(s[ejected]) - FIRST_VALUE] -= 1
	counter_s = counter_s_copy[:]

print(counter_sub)