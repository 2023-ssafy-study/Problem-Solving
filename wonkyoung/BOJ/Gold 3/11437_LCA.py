# 231106
# 124324 KB, 1040 ms (Pypy3)
from sys import stdin

def to_int():
    return int(stdin.readline())

def to_int_map():
    return map(int, stdin.readline().split())

def find_lca(node1, node2, parent, level):
    while level[node1] != level[node2]:
        if level[node1] < level[node2]:
            node2 = parent[node2]
        else:
            node1 = parent[node1]

    if node1 == node2:
        return node1

    while node1 != node2:
        node1 = parent[node1]
        node2 = parent[node2]

    return node2

def fill_arr(node1, node2, parent, level, nodes):
    if parent[node1]:
        parent[node2] = node1
        level[node2] = level[node1] + 1
    elif parent[node2]:
        parent[node1] = node2
        level[node1] = level[node2] + 1
    else:
        nodes.append((node1, node2))


def print_lca():
    from collections import deque
    N = to_int()
    level = [0] * (N + 1)
    parent = [0] * (N + 1)
    link_info = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    parent[1] = -1
    nodes = deque()

    for _ in range(N - 1):
        node1, node2 = to_int_map()
        link_info[node1].append(node2)
        link_info[node2].append(node1)

    nodes.append(1)
    visited[1] = True
    while nodes:
        now = nodes.popleft()
        for next_node in link_info[now]:
            if not visited[next_node]:
                visited[next_node] = True
                parent[next_node] = now
                level[next_node] = level[now] + 1
                nodes.append(next_node)

    M = to_int()
    for _ in range(M):
        print(find_lca(*to_int_map(), parent, level))

print_lca()
