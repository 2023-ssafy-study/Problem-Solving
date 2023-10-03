# 42788 KB 136 ms

import sys

sys.setrecursionlimit(2500)

def dfs(nx, ny):
    if nx == M-1 and ny == N-1:
        return 1
    if DP[nx][ny] > -1:
        return DP[nx][ny]
    
    cnt = 0
    
    for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
        dx, dy = nx+i, ny+j
        if 0 > dx or dx >= M or 0 > dy or dy >= N:
            continue
        # 내리막길로만 이동해야 함
        if board[dx][dy] >= board[nx][ny]:
            continue
        # dx, dy에서 M-1, N-1까지 이동할 수 있는 경로의 수
        cnt += dfs(dx, dy)
        
    DP[nx][ny] = cnt

    return DP[nx][ny]

M, N = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

DP = [[-1]*N for _ in range(M)]

print(dfs(0, 0))