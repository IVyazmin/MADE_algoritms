from sys import setrecursionlimit
import threading
from sys import stdin, stdout

RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26
DEFAULT_COLOR = 0


def dfs(v, adjacency_list, used, tin, up, timer, cutpoints, parent):
    used[v] = 1
    tin[v] = timer[0]
    up[v] = timer[0]
    timer[0] += 1
    children = 0
    for u in adjacency_list[v]:
        if u == parent:
            continue
        if used[u] == 1:
            up[v] = min(up[v], tin[u])
        else:
            dfs(u, adjacency_list, used, tin, up, timer, cutpoints, v)
            up[v] = min(up[v], up[u])
            children += 1
            if up[u] >= tin[v] and parent != -1:
                cutpoints.append(v + 1)
    if parent == -1 and children > 1:
        cutpoints.append(v)


            
def main():
    n, m = map(int, stdin.readline().split())
    adjacency_list = [list() for i in range(n)]
    for i in range(m):
        u, v = map(int, stdin.readline().split())
        if u == v:
            continue
        u -= 1
        v -= 1
        if v not in adjacency_list[u]:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
    
    used = [0] * n
    tin = [0] * n
    up = [0] * n
    timer = [1]
    cutpoints = []
    for v in range(n):
        if used[v] == 0:
        	dfs(v, adjacency_list, used, tin, up, timer, cutpoints, -1)

    stdout.write(str(len(set(cutpoints))) + '\n')
    cutpoints = ' '.join(map(str, sorted(list(set(cutpoints)))))
    stdout.write(cutpoints + '\n')


setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)
thread = threading.Thread(target=main)
thread.start()