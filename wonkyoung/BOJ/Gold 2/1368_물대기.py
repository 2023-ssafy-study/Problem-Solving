# 240415
# 프림
# 39900 KB / 108 ms
from heapq import heappush, heappop

N = int(input())
direct = [int(input()) for _ in range(N)]
link_cost = [list(map(int, input().split())) for _ in range(N)]
heap, visited = [], [False] * N

for i in range(N):
    heappush(heap, (direct[i], i))

cnt = min_cost = 0
while cnt < N:
    cost, num = heappop(heap)
    if not visited[num]:
        visited[num] = True
        cnt += 1
        min_cost += min(cost, direct[num])
        for i in range(N):
            if not visited[i]:
                heappush(heap, (link_cost[num][i], i))

print(min_cost)


# 39892 KB / 112 ms
from heapq import heappush, heappop, heapify

N = int(input())
heap = [(int(input()), i) for i in range(N)]
link_cost = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
heapify(heap)

cnt = min_cost = 0
while cnt < N:
    cost, num = heappop(heap)
    if not visited[num]:
        visited[num] = True
        cnt += 1
        min_cost += cost
        for i in range(N):
            if not visited[i]:
                heappush(heap, (link_cost[num][i], i))

print(min_cost)


# 39904 KB / 108 ms
from heapq import heappush, heappop

N = int(input())
direct = [int(input()) for _ in range(N)]
link_cost = [list(map(int, input().split())) for _ in range(N)]
heap, visited = [], [False] * N

for i in range(N):
    heappush(heap, (direct[i], i))

cnt = min_cost = 0
while cnt < N:
    cost, num = heappop(heap)
    if not visited[num]:
        visited[num] = True
        cnt += 1
        min_cost += cost
        for i in range(N):
            if not visited[i]:
                heappush(heap, (link_cost[num][i], i))

print(min_cost)


# 39904 KB / 108 ms
from heapq import heappush, heappop

N = int(input())
direct = [int(input()) for _ in range(N)]
link_cost = [tuple(map(int, input().split())) for _ in range(N)]
heap, visited = [], [False] * N

for i in range(N):
    heappush(heap, (direct[i], i))

cnt = min_cost = 0
while cnt < N:
    cost, num = heappop(heap)
    if not visited[num]:
        visited[num] = True
        cnt += 1
        min_cost += cost
        for i in range(N):
            if not visited[i]:
                heappush(heap, (link_cost[num][i], i))

print(min_cost)