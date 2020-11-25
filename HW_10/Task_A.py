from sys import setrecursionlimit
import threading
from sys import stdin, stdout

RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOR = 0


def dfs(v, adjacency_list, used, cur_color):
	used[v] = cur_color
	for u in adjacency_list[v]:
		if used[u] == DEFAULT_COLOR:
			dfs(u, adjacency_list, used, cur_color)

            
def main():
    n, m = map(int, stdin.readline().split())
    adjacency_list = [list() for i in range(n)]
    for i in range(m):
    	u, v = map(int, stdin.readline().split())
    	u -= 1
    	v -= 1
    	adjacency_list[u].append(v)
    	adjacency_list[v].append(u)
    
    used = [DEFAULT_COLOR] * n
    cur_color = 0
    for v in range(n):
        if not(used[v]):
        	cur_color += 1
        	dfs(v, adjacency_list, used, cur_color)

    used = ' '.join(map(str, used))
    stdout.write(str(cur_color) + '\n')
    stdout.write(used + '\n')


setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)
thread = threading.Thread(target=main)
thread.start()