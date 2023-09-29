from collections import deque
N = int(input())
dir = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
maps = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    maps[y][x] = 1
    q = deque()
    q.append(d)
    for _ in range(g):
        for i in range(len(q)-1, -1, -1):
            q.append((q[i]+1) % 4)
    while q:
        di, dj = dir[q.popleft()]
        y, x = y + di, x + dj
        if 0 <= x < 101 and 0 <= y < 101:
            maps[y][x] = 1

# 찾기
def check(si, sj):
    curve = 1
    check_dir = [(0, 1), (1, 0), (1, 1)]
    for di, dj in check_dir:
        ci, cj = si + di, sj + dj
        if 0 <= ci < 101 and 0 <= cj < 101 and maps[ci][cj] == 1:
            curve += 1
    if curve == 4:
        return 1
    else:
        return 0
ans = 0
for i in range(101):
    for j in range(101):
        if maps[i][j] == 1:
            ans += check(i, j)
print(ans)