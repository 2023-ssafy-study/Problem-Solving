import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def construct(w):
    if w not in cond:  # 이전에 지어야할 건물이 없을 때
        dp[w] = D[w]
        return
    if dp[w] != -1:  # 이미 건물이 지어졌을 때
        return
    for cw in cond[w]:
        construct(cw)
        dp[w] = max(dp[cw] + D[w], dp[w])

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())  # 건물 개수, 건설 규칙 개수
    D = [-1] + list(map(int, input().split()))  # 건물 당 건설 시간

    cond = {}  # 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능
    for _ in range(K):
        X, Y = map(int, input().split())
        cond[Y] = cond.get(Y, []) + [X]

    dp = [-1] * (N + 1)
    W = int(input())  # 건설해야할 건물
    construct(W)
    print(dp[W])
