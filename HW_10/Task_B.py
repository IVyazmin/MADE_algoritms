from sys import setrecursionlimit
import threading
from sys import stdin, stdout

RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_LENGTH = 2


def dfs(v, adjacency_dict, used, cur_len, max_len):
    used[v] = 1
    max_len = max(max_len, cur_len)
    for u in adjacency_dict[v]:
        if used[u] == 0:
            max_len = dfs(u, adjacency_dict, used, cur_len + 1, max_len)
    return max_len

            
def main():
    n = int(stdin.readline())
    adjacency_dict = dict()
    used = dict()
    queue = list()
    for i in range(n):
        words = stdin.readline().lower().split()
        if words[0] not in adjacency_dict:
            adjacency_dict[words[0]] = []
            used[words[0]] = 0
            queue.append(words[0])
        if words[2] not in adjacency_dict:
            adjacency_dict[words[2]] = []
            used[words[2]] = 0
        adjacency_dict[words[2]].append(words[0])

    max_len = 0
    for v in queue:
        if not(used[v]):
            comp_len = dfs(v, adjacency_dict, used, DEFAULT_LENGTH, max_len)
            max_len = max(max_len, comp_len)

    stdout.write(str(max_len) + '\n')


setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)
thread = threading.Thread(target=main)
thread.start()