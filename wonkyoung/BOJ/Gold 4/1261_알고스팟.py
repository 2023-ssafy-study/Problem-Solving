# 230108
# 33188 KB / 72 ms
from heapq import heappush, heappop

M, N = map(int, input().split())
limit = N * M
maze = [input() for _ in range(N)]
min_cnt = [[limit] * M for _ in range(N)]
min_cnt[0][0] = 0
heap = [(0, 0, 0)]

while heap:
    cnt, y, x = heappop(heap)
    if min_cnt[y][x] >= cnt:
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                new_cnt = cnt if maze[ny][nx] == '0' else cnt + 1
                if new_cnt < min_cnt[ny][nx]:
                    min_cnt[ny][nx] = new_cnt
                    heappush(heap, (new_cnt, ny, nx))

print(min_cnt[-1][-1])



# 33188 KB / 72 ms
from heapq import heappush, heappop

M, N = map(int, input().split())
limit = N * M
maze = [input() for _ in range(N)]
min_cnt = [[limit] * M for _ in range(N)]
min_cnt[0][0] = 0
heap = [(0, 0, 0)]

while heap:
    cnt, y, x = heappop(heap)
    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M:
            new_cnt = cnt if maze[ny][nx] == '0' else cnt + 1
            if new_cnt < min_cnt[ny][nx]:
                min_cnt[ny][nx] = new_cnt
                heappush(heap, (new_cnt, ny, nx))

print(min_cnt[-1][-1])