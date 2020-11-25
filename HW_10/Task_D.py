from sys import setrecursionlimit
import threading
from sys import stdin, stdout

RECURSION_LIMIT = 10 ** 9
STACK_SIZE = 2 ** 26
WHITE = 0
BLACK = 1


def dfs_sort(v, transp_list, used, sorted_list):
    used[v] = BLACK
    for u in transp_list[v]:
        if used[u] == WHITE:
            dfs_sort(u, transp_list, used, sorted_list)
    sorted_list.append(v)
    return 


def dfs_color(v, adjacency_list, used, cur_color):
    used[v] = cur_color
    for u in adjacency_list[v]:
        if used[u] == WHITE:
            dfs_color(u, adjacency_list, used, cur_color)

            
def main():
    n, m = map(int, stdin.readline().split())
    adjacency_list = [list() for i in range(n)]
    transp_list = [list() for i in range(n)]
    for i in range(m):
        u, v = map(int, stdin.readline().split())
        if u == v:
            continue
        u -= 1
        v -= 1
        adjacency_list[u].append(v)
        transp_list[v].append(u)
    
    used = [WHITE] * n
    sorted_list = []
    for v in range(n):
        if used[v] == WHITE:
            dfs_sort(v, transp_list, used, sorted_list)

    sorted_list.reverse()
    used = [WHITE] * n
    cur_color = WHITE
    for v in sorted_list:
        if used[v] == WHITE:
        	cur_color += 1
        	dfs_color(v, adjacency_list, used, cur_color)

    transp_list = [set() for i in range(cur_color)]
    for v in range(n):
        for u in adjacency_list[v]:
            if used[v] != used[u]:
                transp_list[used[v] - 1].add(used[u] - 1)

    count = 0
    for v in range(cur_color):
        count += len(transp_list[v])
    stdout.write(str(count) + '\n')


setrecursionlimit(RECURSION_LIMIT)
threading.stack_size(STACK_SIZE)
thread = threading.Thread(target=main)
thread.start()