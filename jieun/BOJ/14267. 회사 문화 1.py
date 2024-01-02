import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v):
    global comp
    for u in tree[v]:
        comp[u] += comp[v]
        dfs(u)


n, m = map(int, input().split())
sups = tuple(map(int, input().split()))  # 직장 상사 번호, 1번이 사장
tree = [[] for _ in range(n + 1)]  # 직속부하 저장
for i in range(1, n):
    tree[sups[i]].append(i + 1)

comp = [0] * (n + 1)  # 칭찬 받은 정도
for _ in range(m):
    i, w = map(int, input().split())
    comp[i] += w  # 칭찬을 각 사람에게 더해준다

dfs(1)  # 내리 칭찬

for i in range(1, n + 1):
    print(comp[i], end=' ')
