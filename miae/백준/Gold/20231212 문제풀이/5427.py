# 출구 : 바깥으로~!
from collections import deque
from pprint import pprint
T = int(input())

def fire_bfs(q):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = di + ci, dj + cj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            # 벽이거나 방문처리
            if maps[ni][nj] == -1 or fires[ni][nj] != int(1e9):
                continue
            fires[ni][nj] = fires[ci][cj] + 1
            q.append((ni, nj))

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            # 벽이거나 방문처리
            if maps[ni][nj] == -1 or maps[ni][nj] > 0:
                continue
            # 불이 옮겨진칸
            if fires[ni][nj] <= maps[ci][cj] + 1:
                continue
            maps[ni][nj] = maps[ci][cj] + 1
            q.append((ni, nj))

for _ in range(T):
    w, h = map(int, input().split())
    maps = [[0] * w for _ in range(h)]
    fires = [[int(1e9)] * w for _ in range(h)]
    f_q = deque()
    si, sj = 0, 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                # 벽
                maps[i][j] = -1
            elif s[j] == '@':
                maps[i][j] = 1
                si, sj = i, j
            elif s[j] == '*':
                fires[i][j] = 1
                f_q.append((i, j))
    # maps : 상근위치 1 , 벽-불 -1, 빈공간 0
    # fires : 불위치 1, 빈공간 int(1e9)
    fire_bfs(f_q)
    bfs(si, sj)
    ans = int(1e9)
    for i in range(h):
        if maps[i][0] > 0:
            ans = min(maps[i][0], ans)
        if maps[i][w-1] > 0:
            ans = min(maps[i][w-1], ans)
        if i == 0 or i == h-1:
            for j in range(1, w-1):
                if maps[i][j] > 0:
                    ans = min(maps[i][j], ans)
    if ans == int(1e9):
        print('IMPOSSIBLE')
    else:
        print(ans)