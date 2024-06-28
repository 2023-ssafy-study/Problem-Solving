# 240628
# 344956 KB / 5328 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
max_cost = 1001
road_info = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = to_int()
    road_info[A].append((C, B))
    road_info[B].append((C, A))

cnt = 0
heap = []
for element in road_info[1]:
    heappush(heap, element)

visited = [False] * (N+1)
visited[1] = True
road_cost_list = []
while cnt < N-1:
    cost, house = heappop(heap)
    if not visited[house]:
        road_cost_list.append(cost)
        visited[house] = True
        cnt += 1
        for new_cost, new_house in road_info[house]:
            if not visited[new_house]:
                heappush(heap, (new_cost, new_house))

print(sum(road_cost_list) - max(road_cost_list))



# 344172 KB / 6040 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
road_info = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = to_int()
    road_info[A].append((C, B))
    road_info[B].append((C, A))

cnt = 0
heap = []
for element in road_info[1]:
    heappush(heap, element)

visited = [False] * (N+1)
visited[1] = True
min_total = max_cost = 0
while cnt < N-1:
    cost, house = heappop(heap)
    if not visited[house]:
        min_total += cost
        visited[house] = True
        cnt += 1
        if cost > max_cost:
            max_cost = cost
        for new_cost, new_house in road_info[house]:
            if not visited[new_house]:
                heappush(heap, (new_cost, new_house))

print(min_total - max_cost)



# 344956 KB / 5928 ms

from sys import stdin
from heapq import heappush, heappop, heapify

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
road_info = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = to_int()
    road_info[A].append((C, B))
    road_info[B].append((C, A))

cnt = 0
heap = road_info[1][:]
heapify(heap)

visited = [False] * (N+1)
visited[1] = True
road_cost_list = []
while cnt < N-1:
    cost, house = heappop(heap)
    if not visited[house]:
        road_cost_list.append(cost)
        visited[house] = True
        cnt += 1
        for new_cost, new_house in road_info[house]:
            if not visited[new_house]:
                heappush(heap, (new_cost, new_house))

print(sum(road_cost_list) - max(road_cost_list))
