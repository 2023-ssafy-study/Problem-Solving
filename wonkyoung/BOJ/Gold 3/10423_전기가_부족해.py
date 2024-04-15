# 240415
# 프림
# 62160 KB / 308 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
city_link = [[] for _ in range(N+1)]
start_list = list(to_int())
for _ in range(M):
    u, v, w = to_int()
    city_link[u].append((w, v))
    city_link[v].append((w, u))

heap = []
visited = [False] * (N+1)
visited_cnt, min_cost = K, 0
for u in start_list:
    visited[u] = True
    for w, v in city_link[u]:
        if not visited[v]:
            heappush(heap, (w, v))

while visited_cnt < N:
    w, u = heappop(heap)
    if not visited[u]:
        visited[u] = True
        visited_cnt += 1
        min_cost += w
        for w, v in city_link[u]:
            if not visited[v]:
                heappush(heap, (w, v))

print(min_cost)


# 56780 KB / 388 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

N, M, K = to_int()
city_link = [[] for _ in range(N+1)]
start_list = list(to_int())
for _ in range(M):
    u, v, w = to_int()
    city_link[u].append((w, v))
    city_link[v].append((w, u))

heap = []
visited = [False] * (N+1)
visited_cnt, min_cost = K, 0
for u in start_list:
    visited[u] = True
    for element in city_link[u]:
        heappush(heap, element)

while visited_cnt < N:
    w, u = heappop(heap)
    if not visited[u]:
        visited[u] = True
        visited_cnt += 1
        min_cost += w
        for element in city_link[u]:
            heappush(heap, element)

print(min_cost)