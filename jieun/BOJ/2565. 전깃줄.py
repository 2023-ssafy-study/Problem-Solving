ea = int(input())
connected = sorted([tuple(map(int, input().split())) for _ in range(ea)])

dp = [1] * ea
for i in range(1, ea):
    for j in range(i):
        if connected[j][1] < connected[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(ea - max(dp))
