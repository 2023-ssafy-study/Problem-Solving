# 240408
# 31120 KB / 1984 ms
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_val = 0

def in_range(y, x):
    if 0 <= y < N and 0 <= x < M and not visited[y][x]:
        visited[y][x] = True
        return True

    return False

def choose(y, x, val):
    global max_val
    if max_val < val:
        max_val = val

    new_val = val
    for i in range(y, N):
        for j in range(M):
            if in_range(i, j):
                new_val += 2*arr[i][j]
                for di in (-1, 1):
                    ni = i+di
                    if in_range(ni, j):
                        new_val += arr[ni][j]
                        for dj in (-1, 1):
                            nj = j+dj
                            if in_range(i, nj):
                                new_val += arr[i][nj]
                                choose(i, j, new_val)
                                visited[i][nj] = False
                                new_val -= arr[i][nj]
                        visited[ni][j] = False
                        new_val -= arr[ni][j]
                visited[i][j] = False
                new_val -= 2 * arr[i][j]


choose(0, 0, 0)

print(max_val)


# 31120 KB / 1976 ms
N, M = map(int, input().split())
loaf = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_total = 0

def in_range(y, x):
    if 0 <= y < N and 0 <= x < M and not visited[y][x]:
        visited[y][x] = True
        return True
    return False

def dfs(level, y, x, total):
    global max_total
    if level == 0:
        for i in range(y, N):
            for j in range(M):
                if in_range(i, j):
                    dfs(1, i, j, total+2*loaf[i][j])
                    visited[i][j] = False
    elif level == 1:
        for i in (-1, 1):
            ny = y+i
            if in_range(ny, x):
                dfs(2, y, x, total+loaf[ny][x])
                visited[ny][x] = False
    else:
        for j in (-1, 1):
            nx = x+j
            if in_range(y, nx):
                new_total = total + loaf[y][nx]
                dfs(0, y, x, new_total)
                if new_total > max_total:
                    max_total = new_total
                visited[y][nx] = False

dfs(0, 0, 0, 0)

print(max_total)
