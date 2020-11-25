from sys import setrecursionlimit
import threading
from sys import stdin, stdout

RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26
WHITE = 0
GREY = 1
BLACK = 2


def dfs(v, adjacency_list, used, sorted_list):
	used[v] = GREY
	for u in adjacency_list[v]:
		if used[u] == GREY:
			return 1
		if used[u] == WHITE:
			if dfs(u, adjacency_list, used, sorted_list):
				return 1
	used[v] = BLACK
	sorted_list.append(v)
	return 0

            
def main():
    n, m = map(int, stdin.readline().split())
    adjacency_list = [list() for i in range(n)]
    for i in range(m):
    	u, v = map(int, stdin.readline().split())
    	u -= 1
    	v -= 1
    	adjacency_list[u].append(v)
    
    used = [WHITE] * n
    sorted_list = []
    for v in range(n):
        if used[v] == WHITE:
        	has_cycle = dfs(v, adjacency_list, used, sorted_list)
        	if has_cycle:
        		break
    if has_cycle:
    	stdout.write('-1')
    else:
	    sorted_list = [v + 1 for v in sorted_list]
	    sorted_list.reverse()
	    sorted_list = ' '.join(map(str, sorted_list))
	    stdout.write(sorted_list + '\n')


setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)
thread = threading.Thread(target=main)
thread.start()