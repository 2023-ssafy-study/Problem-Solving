N, X = map(int, input().split())
memo = {}
memo[0] = 1
p = {}
p[0] = 1
for i in range(1, N+1):
    memo[i] = memo[i-1] * 2 + 3
    p[i] = p[i-1] * 2 + 1

def solve(n, x):
    if n == 0: # 패티한개
        return 1
    if x == 1: # 번
        return 0
    elif x <= 1 + memo[n-1]: # 중간 이전
        return solve(n-1, x-1)
    elif x == 2 + memo[n-1]: # 중간까지
        return p[n-1] + 1
    elif x <= 2 * memo[n-1] + 2: # 중간 이후
        return p[n-1] + 1 + solve(n-1, x - memo[n-1] - 2)
    else: # 다 먹음
        return p[n]
ans = solve(N, X)
print(ans)