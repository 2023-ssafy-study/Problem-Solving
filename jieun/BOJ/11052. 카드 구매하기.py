N = int(input())
p = tuple(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(N + 1):
    for j in range(i):
        dp[i] = max(dp[i - j - 1] + p[j], dp[i])

print(dp[N])
