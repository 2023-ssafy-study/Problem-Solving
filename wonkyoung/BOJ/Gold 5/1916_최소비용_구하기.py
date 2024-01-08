# 230108
# 57372 KB / 316 ms
from sys import stdin
from heapq import heappush, heappop

def to_int(): return int(stdin.readline())
def to_int_map(): return map(int, stdin.readline().split())

N = to_int()
M = to_int()
limit = int(1e8)
city_route = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = to_int_map()
    city_route[start].append((cost, end))

start, end = to_int_map()
min_cost = [limit] * (N+1) # 출발 도시에서 각 도시까지 가는 데 드는 최소 비용
min_cost[start] = 0
heap = [(0, start)]

while heap:
    cost, city = heappop(heap) # 비용, 도착 도시
    if cost <= min_cost[city]:
        for next_cost, next_city in city_route[city]:
            new_cost = next_cost + cost
            if new_cost < min_cost[next_city]:
                heappush(heap, (new_cost, next_city))
                min_cost[next_city] = new_cost

print(min_cost[end])
