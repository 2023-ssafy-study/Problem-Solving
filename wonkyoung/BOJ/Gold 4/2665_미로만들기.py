# 230108
# 34052 KB / 184 ms
from collections import deque
N = int(input())
room_list = [input() for _ in range(N)] # 각 방의 상태

square = N*N + 1
cnt_list = [[square] * N for _ in range(N)] # 각 방까지 가기 위해 바꿔야 하는 방의 개수
visited = [[False] * N for _ in range(N)] # 방을 방문했는지 여부

q = deque()
q.append((0, 0, 0))
cnt_list[0][0] = 0
visited[0][0] = True


while q:
    y, x, cnt = q.popleft()
    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < N:
            new_cnt = cnt if room_list[ny][nx] == '1' else cnt+1
            if not visited[ny][nx] or cnt_list[ny][nx] > new_cnt:
                visited[ny][nx] = True
                q.append((ny, nx, new_cnt))
                cnt_list[ny][nx] = new_cnt

print(cnt_list[-1][-1])



# 34184 KB / 168 ms
from collections import deque
N = int(input())
room_list = [input() for _ in range(N)] # 각 방의 상태

square = N*N + 1
cnt_list = [[square] * N for _ in range(N)] # 각 방까지 가기 위해 바꿔야 하는 방의 개수

q = deque()
q.append((0, 0, 0))
cnt_list[0][0] = 0


while q:
    y, x, cnt = q.popleft()
    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < N:
            new_cnt = cnt if room_list[ny][nx] == '1' else cnt+1
            if cnt_list[ny][nx] > new_cnt: # 바꿔야 하는 방 개수가 기존 개수보다 작으면
                q.append((ny, nx, new_cnt))
                cnt_list[ny][nx] = new_cnt

print(cnt_list[-1][-1])


# 33320 KB / 52 ms
from heapq import heappush, heappop
N = int(input())
room_list = [input() for _ in range(N)] # 각 방의 상태

heap = [(0, 0, 0)]
square = N*N + 1
cnt_list = [[square] * N for _ in range(N)] # 각 방까지 가기 위해 바꿔야 하는 방의 개수

while heap:
    cnt, y, x = heappop(heap)
    if cnt <= cnt_list[y][x]: # 현재 위치 기준 바꿔야 하는 방 개수가 기존 개수보다 작거나 같으면
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                new_cnt = cnt if room_list[ny][nx] == '1' else cnt+1
                if new_cnt < cnt_list[ny][nx]: # 바꿔야 하는 방 개수가 기존 개수보다 작으면
                    heappush(heap, (new_cnt, ny, nx))
                    cnt_list[ny][nx] = new_cnt

print(cnt_list[-1][-1])



# 33188 KB / 56 ms
from heapq import heappush, heappop
N = int(input())
room_list = [input() for _ in range(N)] # 각 방의 상태

heap = [(0, 0, 0)]
square = N*N + 1
cnt_list = [[square] * N for _ in range(N)] # 각 방까지 가기 위해 바꿔야 하는 방의 개수
cnt_list[0][0] = 0

while heap:
    cnt, y, x = heappop(heap)
    if cnt <= cnt_list[y][x]:
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                new_cnt = cnt if room_list[ny][nx] == '1' else cnt+1
                if new_cnt < cnt_list[ny][nx]:
                    heappush(heap, (new_cnt, ny, nx))
                    cnt_list[ny][nx] = new_cnt

print(cnt_list[-1][-1])



# 33188 KB / 52 ms
def min_cnt():
    from heapq import heappush, heappop
    N = int(input())
    room_list = [input() for _ in range(N)]

    heap = [(0, 0, 0)]
    square = N * N + 1
    cnt_list = [[square] * N for _ in range(N)]

    while heap:
        cnt, y, x = heappop(heap)
        if cnt <= cnt_list[y][x]:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < N:
                    new_cnt = cnt if room_list[ny][nx] == '1' else cnt + 1

                    if new_cnt < cnt_list[ny][nx]:
                        heappush(heap, (new_cnt, ny, nx))
                        cnt_list[ny][nx] = new_cnt

    return cnt_list[-1][-1]

print(min_cnt())


# 33188 KB / 52 ms
def min_cnt():
    from heapq import heappush, heappop
    N = int(input())
    room_list = [input() for _ in range(N)]

    heap = [(0, 0, 0)]
    square = N * N
    cnt_list = [[square] * N for _ in range(N)]

    while heap:
        cnt, y, x = heappop(heap)
        if cnt <= cnt_list[y][x]:
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y + dy, x + dx

                if 0 <= ny < N and 0 <= nx < N:
                    new_cnt = cnt if room_list[ny][nx] == '1' else cnt + 1

                    if new_cnt < cnt_list[ny][nx]:
                        heappush(heap, (new_cnt, ny, nx))
                        cnt_list[ny][nx] = new_cnt

    return cnt_list[-1][-1]


print(min_cnt())