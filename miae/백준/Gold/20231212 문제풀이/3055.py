from collections import deque
R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
water = [[0 for _ in range(C)] for _ in range(R)]
q = deque()
visit = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == 'D':
            ei, ej = i, j
        elif board[i][j] == 'S':
            si, sj = i, j
        elif board[i][j] == 'X':
            water[i][j] = -1
        elif board[i][j] == '*':
            water[i][j] = 1
            visit[i][j] = 1
            q.append((i, j, 1))

# 물 맵
while q:
    ci, cj, cv = q.popleft()
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni, nj = di + ci, dj + cj
        if not (0 <= ni < R and 0 <= nj < C):
            continue
        if board[ni][nj] == 'X' or visit[ni][nj] == 1:
            continue
        if board[ni][nj] == 'D':
            continue
        visit[ni][nj] = 1
        water[ni][nj] = cv+1
        q.append((ni, nj, cv+1))

# 고슴도치 이동
sq = deque()
sq.append((si, sj, 1))
visit[si][sj] = 2
while sq:
    ci, cj, cv = sq.popleft()
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni, nj = di + ci, dj + cj
        if not (0 <= ni < R and 0 <= nj < C):
            continue
        if board[ni][nj] == 'D':
            print(cv)
            exit()
        if board[ni][nj] == 'X' or visit[ni][nj] == 2:
            continue
        if water[ni][nj] == 0 or water[ni][nj] > cv+1:
            visit[ni][nj] = 2
            sq.append((ni, nj, cv+1))
print('KAKTUS')