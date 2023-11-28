from pprint import pprint
memo = [[0] * 2001 for _ in range(11)]
memo[0][0] = 1 # 0으로 만들 수 있는 경우의 수
for i in range(1, 11):
    for j in range(1, 2001):
        for k in range(j//2+1):
            memo[i][j] += memo[i-1][k]
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    ans = 0
    for l in range(2**(n-1), m+1):
        ans += memo[n][l]
    print(ans)
