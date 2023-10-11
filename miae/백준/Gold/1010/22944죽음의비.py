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
    q.append((si, sj, H, 0, 0))
    visit[si][sj] = H
    while q:
        ci, cj, ch, cd, cnt = q.popleft()
        nh, nd = ch, cd
        if ch == 0:
            continue
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if ni == ei and nj == ej:
                return cnt + 1
            if board[ni][nj] == 'U':
                nd = D-1
            elif board[ni][nj] == '.':
                if cd > 0:
                    nd -= 1
                else:
                    nh -= 1
            if visit[ni][nj] < nh:
                visit[ni][nj] = nh
                q.append((ni, nj, nh, nd, cnt+1))
    return -1
print(bfs())