# 231212
# 34132 KB / 68 ms
def find_min_cnt():
    from collections import deque
    R, C = map(int, input().split())
    forest = [list(input()) for _ in range(R)]

    q = deque()

    for i in range(R):
        for j in range(C):
            position = forest[i][j]
            if position == '*':
                q.append((i, j, 1, 0))
            elif position == 'S':
                start = (i, j, 2, 0)
            elif position == 'D':
                final_y, final_x = i, j

    q.append(start)

    def bfs():
        not_passed = {'*', 'X'}
        visited = [[False] * C for _ in range(R)]
        visited[start[0]][start[1]] = True

        while q:
            y, x, type_of, cnt = q.popleft()
            if final_y == y and final_x == x:
                return cnt
            if type_of == 1:
                for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C and forest[ny][nx] == '.':
                        forest[ny][nx] = '*'
                        q.append((ny, nx, 1, cnt + 1))
            else:
                for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C:
                        if forest[ny][nx] not in not_passed and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx, 2, cnt + 1))
        return 'KAKTUS'

    return bfs()

print(find_min_cnt())