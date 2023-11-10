from collections import defaultdict as dd
import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000)
# pypy는 깊이를 대략적인 값으로, Python은 정확하게 정의함.

N = int(input())
tree = dd(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depths = [-1] * (N + 1)  # 깊이
parent = [-1] * (N + 1)  # 부모 노드


def dfs(v, depth):
    if depths[v] != -1: return
    depths[v] = depth
    for u in tree[v]:
        if parent[u] != -1: continue
        parent[u] = v
        dfs(u, depth + 1)


dfs(1, 0)


def lca(a, b):
    # 깊이를 맞춘다: 더 깊은 노드는 그의 부모로 노드를 바꿔준다
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 거슬러 올라가며 공통 조상 찾기
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
