N, K = map(int, input().split())
A = list(map(int, input().split()))
# 누적합
total = 0
# 해쉬
memo = {}
memo[0] = 1
ans = 0
for i in range(N):
    total += A[i]
    # 현재까지의 누적합 dp[i] - dp[이전누적값] == k 이면 추가
    if total - K in memo:
        ans += memo[total - K]
    # 이전 누적값 메모이제이션
    if total not in memo:
        memo[total] = 1
    else:
        memo[total] += 1
print(ans)