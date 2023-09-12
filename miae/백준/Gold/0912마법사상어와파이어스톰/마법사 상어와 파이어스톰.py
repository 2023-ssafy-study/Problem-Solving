from copy import deepcopy
from collections import deque
def ice(si, sj):
    if rot[si][sj] == 0:
        return 0
    cnt = 0
    for di, dj in dir:
        ci, cj = si + di, sj + dj
        if (0 <= ci < M and 0 <= cj < M) and rot[ci][cj] != 0:
            cnt += 1

    return cnt

def check(si, sj):
    q = deque()
    q.append((si, sj))
    visit[si][sj] = 1
    ret = 1
    while q:
        ni, nj = q.popleft()
        for di, dj in dir:
            ci, cj = ni + di, nj + dj
            if (0 <= ci < M and 0 <= cj < M) and maps[ci][cj] != 0 and visit[ci][cj] == 0:
                visit[ci][cj] = 1
                ret += 1
                q.append((ci, cj))
    return ret


# 분할 정복 - 격자돌리기
def solve(si, sj):
    global rot
    for i in range(L):
        for j in range(L):
            rot[si+j][sj+L-1-i] = maps[si+i][sj+j]
    return

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, Q = map(int, input().split())
M = 2 ** N
rot = [[0] * M for _ in range(M)]
maps = [list(map(int, input().split())) for _ in range(M)]
L_lst = list(map(int, input().split()))
for i in range(Q):
    # 시전방법

    L = 2 ** L_lst[i]
    for y in range(0, M, L):
        for x in range(0, M, L):
           solve(y, x)
    maps = deepcopy(rot)
    for y in range(M):
        for x in range(M):
            if maps[y][x] > 0 and ice(y, x) < 3:
                maps[y][x] -= 1
ans = 0
ans2 = 0
visit = [[0] * M for _ in range(M)]
for i in range(M):
    for j in range(M):
        if maps[i][j] > 0:
            ans += maps[i][j]
            ans2 = max(ans2, check(i, j))
print(ans)
print(ans2)