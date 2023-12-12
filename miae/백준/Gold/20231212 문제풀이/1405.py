N, *lst = map(int, input().split())
board = [[0] * (2*N+1) for _ in range(2*N+1)]
board[N][N] = 1
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
ans = 0
def dfs(n, ci, cj, num):
    global board, ans
    if n == N:
        ans += num
        return
    for i in range(4):
        ni, nj = ci + d[i][0], cj + d[i][1]
        p = lst[i]/100
        if board[ni][nj] == 0:
            board[ni][nj] = 1
            dfs(n+1, ni, nj, num*p)
            board[ni][nj] = 0

dfs(0, N, N, 1)
print(ans)