# 240827
def main():
    from collections import deque
    
    def in_range(y, x):
        return 0 <= y < N and 0 <= x < N
    
    def fill_edges():
        while q:
            y, x = q.popleft()
            if islands[y][x] == 0:
                islands[y][x] = limit
                is_edge = False
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if in_range(ny, nx):
                        if nation[ny][nx] == '0':
                            is_edge = True
                        elif islands[ny][nx] == 0:
                            q.append((ny, nx))
    
                if is_edge:
                    edges[-1].append((y, x, 0))
    
    def find_shortest(edge, num):
        visited = [[False] * N for _ in range(N)]
        while edge:
            y, x, length = edge.popleft()
            if not visited[y][x]:
                visited[y][x] = True
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if in_range(ny, nx) and not visited[ny][nx]:
                        if islands[ny][nx] == 0:
                            edge.append((ny, nx, length+1))
                        elif islands[ny][nx] != num:
                            return length


    N = int(input())
    nation = [input().split() for _ in range(N)]
    islands = [[0] * N for _ in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q, edges = deque(), [deque()]
    limit = 1
    shortest_len = N * N
    
    
    for i in range(N):
        for j in range(N):
            if islands[i][j] == 0 and nation[i][j] == '1':
                q.append((i, j))
                edges.append(deque())
                fill_edges()
                limit += 1
    
    for i in range(1, limit):
        shortest_len = min(shortest_len, find_shortest(edges[i], i))
    
    return shortest_len

print(main())
