# 231229
# 88 ms / 31120 KB
from sys import stdin
new_input = stdin.readline

T = int(new_input())
for _ in range(T):
    N = int(new_input())
    parents = [0] * (N+1)
    level = [0] * (N+1)
    for _ in range(N-1):
        parent, child = map(int, new_input().split())
        parents[child] = parent

    for i in range(1, N+1):
        node = parents[i]
        if node:
            while node > i:
                level[i] += 1
                node = parents[node]
                if not node:
                    break
            else:
                level[i] += level[node]+1

    node1, node2 = map(int, new_input().split())
    limit = level[node1] - level[node2]
    if limit < 0:
        node1, node2 = node2, node1
        limit = -limit

    for _ in range(limit):
        node1 = parents[node1]

    while node1 != node2:
        node1, node2 = parents[node1], parents[node2]

    print(node1)


# 76 ms / 31120 KB
from sys import stdin
new_input = stdin.readline

T = int(new_input())

def find_nca(N):
    parents = [0] * (N + 1)
    level = [0] * (N + 1)
    for _ in range(N - 1):
        parent, child = map(int, new_input().split())
        parents[child] = parent

    node1, node2 = map(int, new_input().split())

    for i in range(1, N + 1):
        node = parents[i]
        if node:
            while node > i:
                level[i] += 1
                node = parents[node]
                if not node:
                    break
            else:
                level[i] += level[node] + 1

    limit = level[node1] - level[node2]
    if limit < 0:
        node1, node2 = node2, node1
        limit = -limit

    for _ in range(limit):
        node1 = parents[node1]

    while node1 != node2:
        node1, node2 = parents[node1], parents[node2]

    return node1

for _ in range(T):
    N = int(new_input())
    print(find_nca(N))


# 76 ms / 31120 KB
from sys import stdin
new_input = stdin.readline

T = int(new_input())

def find_nca(N, node1, node2):
    for i in range(1, N + 1):
        node = parents[i]
        if node:
            while node > i:
                level[i] += 1
                node = parents[node]
                if not node:
                    break
            else:
                level[i] += level[node] + 1

    limit = level[node1] - level[node2]
    if limit < 0:
        node1, node2 = node2, node1
        limit = -limit

    for _ in range(limit):
        node1 = parents[node1]

    while node1 != node2:
        node1, node2 = parents[node1], parents[node2]

    return node1

for _ in range(T):
    N = int(new_input())
    parents = [0] * (N + 1)
    level = [0] * (N + 1)

    for _ in range(N - 1):
        parent, child = map(int, new_input().split())
        parents[child] = parent

    print(find_nca(N, *map(int, new_input().split())))