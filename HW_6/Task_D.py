string_1 = input()
string_2 = input()

seq_lengths = []
seq_lengths.append(list(range(len(string_2) + 1)))
for i in range(len(string_1)):
	seq_lengths.append([i + 1] * (len(string_2) + 1))

for i in range(1, len(string_1) + 1):
	for j in range(1, len(string_2) + 1):
		if string_1[i - 1] == string_2[j - 1]:
			seq_lengths[i][j] = seq_lengths[i - 1][j - 1]
		else:
			seq_lengths[i][j] = min(seq_lengths[i - 1][j], seq_lengths[i][j - 1], seq_lengths[i - 1][j - 1]) + 1

print(seq_lengths[-1][-1])