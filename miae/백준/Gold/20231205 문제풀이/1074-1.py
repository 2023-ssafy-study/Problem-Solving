n, r, c = map(int, input().split())
ans = 0

while n != 0:
    n -= 1
    N = 2 ** n
    if r < N and c < N: # 2사분면
        ans += 0
    elif r < N and c >= N: #1사분면
        ans += (N * N)
        c -= N # N만큼 왼쪽으로
    elif r  >= N and c < N: #3사분면
        ans += (N * N) * 2
        r -= N # N만큼 위쪽으로
    else:
        ans += (N * N) * 3
        c -= N
        r -= N
print(ans)