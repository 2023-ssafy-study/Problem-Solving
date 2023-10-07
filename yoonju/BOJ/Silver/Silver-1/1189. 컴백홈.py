# 31256 KB 132 ms

import sys

def dfs(level, x, y):
    global answer
    # K보다 거리가 멀어지면 백트래킹
    if level > K:
        return
    if level == K and x == 0 and y == C-1:
        answer += 1
        return

    for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
        dx, dy = x+i, y+j
        if 0 > dx or R <= dx or 0 > dy or C <= dy:
            continue
        if visit[dx][dy] or board[dx][dy] == 'T':
            continue
        visit[dx][dy] = True
        dfs(level+1, dx, dy)
        visit[dx][dy] = False

# R*C, 거리가 K인 가짓수 구하기
R, C, K = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

visit = [[False]*C for _ in range(R)]

# 출발 위치 visit 체크! (체크하지 않아 90% 대에서 오답 경험)
visit[R-1][0] = True

answer = 0

# 출발 위치 = R-1, 0
# 도착 위치 = 0, C-1
dfs(1, R-1, 0)

print(answer)