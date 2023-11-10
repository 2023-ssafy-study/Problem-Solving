import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(v):
    visited[v] = True
    for friend in tree[v]:
        if visited[friend]: continue
        find(friend)
        dp[v][0] += dp[friend][1]  # 본인이 얼리어답터가 아니면 자식 노드가 모두 얼리어답터
        dp[v][1] += min(dp[friend])  # 본인이 얼리어답터이면 자식노드의 얼리어답터 여부가 상관 x


N = int(input())
tree = defaultdict(list)
visited = [False] * (N + 1)
dp = [[0, 1] for _ in range(N + 1)]
# 자신이 얼리어답터가 아닐 때, 맞을 때(얼리어답터에 자신을 포함한 값)

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 트리 특성 상 사이클이 없어 어느 노드를 루트로 설정해도 밑의 부분 트리들은 서로 영향을 끼치지 않는다
find(1)  # 루트 노드를 1로 두고 푼다
print(min(dp[1]))
