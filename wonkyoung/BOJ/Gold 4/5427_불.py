# 231212
# 68868 KB / 1880 ms
from sys import stdin
from collections import deque
new_input = stdin.readline
T = int(new_input())

def bfs():
    direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    time = 0
    limit1, limit2 = len(q) - 1, 1

    while q:
        time += 1
        for _ in range(limit1):
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w:
                    if building[ny][nx] == '.':
                        building[ny][nx] = '*'
                        q.append((ny, nx))

        limit1 = len(q) - limit2

        for _ in range(limit2):
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w:
                    if not visited[ny][nx] and building[ny][nx] == '.':
                        visited[ny][nx] = True
                        q.append((ny, nx))
                else:
                    return time

        limit2 = len(q) - limit1
        if limit2 == 0:
            return 'IMPOSSIBLE'

    return 'IMPOSSIBLE'


for _ in range(T):
    w, h = map(int, new_input().split())
    building = [list(new_input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                q.append((i, j))
            elif building[i][j] == '@':
                building[i][j] = '.'
                visited[i][j] = True
                start = (i, j)
    q.append(start)
    print(bfs())


# 68872 KB / 1864 ms
from sys import stdin
from collections import deque
new_input = stdin.readline
T = int(new_input())
direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs():
    time = 0
    limit1, limit2 = len(q) - 1, 1

    while q:
        time += 1
        for _ in range(limit1):
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w:
                    if building[ny][nx] == '.':
                        building[ny][nx] = '*'
                        q.append((ny, nx))

        limit1 = len(q) - limit2

        for _ in range(limit2):
            y, x = q.popleft()
            for dy, dx in direct:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w:
                    if not visited[ny][nx] and building[ny][nx] == '.':
                        visited[ny][nx] = True
                        q.append((ny, nx))
                else:
                    return time

        limit2 = len(q) - limit1
        if limit2 == 0:
            return 'IMPOSSIBLE'

    return 'IMPOSSIBLE'


for _ in range(T):
    w, h = map(int, new_input().split())
    building = [list(new_input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                q.append((i, j))
            elif building[i][j] == '@':
                building[i][j] = '.'
                visited[i][j] = True
                start = (i, j)
    q.append(start)
    print(bfs())