from collections import deque


def bfs():
    while loc:
        sign, r, c = loc.popleft()
        for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            if 0 <= nr < h and 0 <= nc < w:
                if visited[nr][nc] == -1 and building[nr][nc] == '.':
                    if sign == 'S':
                        visited[nr][nc] = visited[r][c] + 1
                    else:
                        building[nr][nc] = '*'
                    loc.append((sign, nr, nc))
            else:
                if sign == 'S':
                    return visited[r][c] + 1
    return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    building = []
    visited = [[-1] * w for _ in range(h)]
    loc = deque()  # 불과 상근이의 위치
    sg = ()  # 상근이의 초기 위치

    for r in range(h):
        building.append(list(input()))
        for c in range(w):
            if building[-1][c] == '*':
                loc.append(('F', r, c))
            elif building[-1][c] == '@':
                sg = ('S', r, c)
                building[-1][c] = '.'
                visited[r][c] = 0
    loc.append(sg)

    print(bfs())
