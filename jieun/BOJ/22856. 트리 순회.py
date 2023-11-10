import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def dfs_r(v):
    global cnt_r
    visited[v] = True
    right = tree[v][1]
    if not visited[right] and right != -1:
        dfs_r(right)
        cnt_r += 1


N = int(input())
tree = {}
for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = (b, c)

# 모든 노드들의 이동 길이 구하기
cnt_a = N-1

# 오른쪽으로만 이동한 길이 구하기
visited = [False] * (N + 1)
cnt_r = 0
dfs_r(1)

print(cnt_a * 2 - cnt_r)
