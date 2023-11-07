import sys

sys.setrecursionlimit(50000)

def dfs(node, d):
    if depth[node] >= 0:
        return

    depth[node] = d

    for child in tree[node]:
        # 노드별 부모 기록
        if parent[child] == -1:
            parent[child] = node
        dfs(child, d+1)

def find_lca(a, b):
    # 두 노드의 깊이 맞추기
    # 더 깊이가 큰 노드 => 부모 노드로 교체
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        elif depth[b] > depth[a]:
            b = parent[b]

    # 두 노드가 같아질 때까지 부모 노드로 교체
    # 같아짐 => 최소 조상 노드 발견
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
depth = [-1]*(N+1)
parent = [-1]*(N+1)
# 루트 표시
parent[1] = 0

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# 노드별 깊이 찾기
dfs(1, 0)

M = int(sys.stdin.readline())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(find_lca(a, b))