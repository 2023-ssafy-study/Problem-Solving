from collections import deque


def bfs(hr, hc):
    dist = [[-1] * C for _ in range(R)]
    dist[hr][hc] = 0
    while loc:
        r, c = loc.popleft()
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if forest[nr][nc] in {'.', 'D'} and forest[r][c] == 'S':
                    if forest[nr][nc] == 'D':  # 비버의 굴 도착 확인
                        return dist[r][c] + 1
                    loc.append((nr, nc))
                    forest[nr][nc] = 'S'
                    dist[nr][nc] = dist[r][c] + 1
                elif forest[nr][nc] in {'.', 'S'} and forest[r][c] == '*':
                    loc.append((nr, nc))
                    forest[nr][nc] = '*'
    return 'KAKTUS'


R, C = map(int, input().split())
hedgehog = ()  # 고슴도치의 초기 위치
loc = deque()  # 고슴도치, 물의 위치

forest = []
for r in range(R):
    forest.append(list(input()))
    for c in range(C):
        if forest[-1][c] == 'S':
            hedgehog = (r, c)
        elif forest[-1][c] == '*':
            loc.append((r, c))
loc.appendleft(hedgehog)

print(bfs(*hedgehog))
