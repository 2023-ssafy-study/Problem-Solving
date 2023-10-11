R, C, K = map(int, input().split())
maps = [list(map(str, input().strip())) for _ in range(R)]
visit = [[0] * C for _ in range(R)]
ans = 0
si, sj = R-1, 0
ei, ej = 0, C-1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def solve(i, j):
    global ans, visit
    if i == ei and j == ej:
        if visit[i][j] == K:
            ans += 1
            return
    for di, dj in dirs:
        ni, nj = di + i, dj + j
        if not (0 <= ni < R and 0 <= nj < C):
            continue
        if visit[ni][nj] == 0 and maps[ni][nj] != 'T':
            visit[ni][nj] = visit[i][j] + 1
            solve(ni, nj)
            visit[ni][nj] = 0

visit[si][sj] = 1
solve(si, sj)
print(ans)