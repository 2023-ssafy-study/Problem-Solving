from sys import stdin

input = stdin.readline

N = int(input())
nums = input().split()

dp = [[0] * N for _ in range(N)]
for c in range(N):
    for r in range(N):
        if r > c:
            break
        if r == c:
            dp[r][c] = 1
        elif nums[r] == nums[c] and (r + 1 == c or dp[r + 1][c - 1] == 1):  # 길이가 2일 때 or 중간 팰린드롬
            dp[r][c] = 1

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
