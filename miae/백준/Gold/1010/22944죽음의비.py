from collections import deque
N, H, D = map(int, input().split())
board = []
si, sj, ei, ej = 0, 0, 0, 0
for i in range(N):
    board.append(list(map(str, input().strip())))
    for j in range(N):
        if board[i][j] == 'S':
            si, sj = i, j
        if board[i][j] == 'E':
            ei, ej = i, j

visit = [[0] * N for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    global visit
    q = deque()
    q.append((si, sj, H, 0))
    visit[si][sj] = 1
    while q:
        ci, cj, ch, cd = q.popleft()
        if ch == 0:
            continue
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if visit[ni][nj] > 0:
                continue
            if board[ni][nj] == 'U':
                visit[ni][nj] = visit[ci][cj] + 1
                q.append((ni, nj, ch, D-1))
            elif board[ni][nj] == '.':
                visit[ni][nj] = visit[ci][cj] + 1
                nh, nd = ch, cd
                if cd > 0:
                    nd -= 1
                else:
                    nh -= 1
                q.append((ni, nj, nh, nd))
            else:
                visit[ni][nj] = visit[ci][cj] + 1
                return

bfs()
print(visit[ei][ej] - 1)