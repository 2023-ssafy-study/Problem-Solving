import heapq, sys

input = sys.stdin.readline


def dijkstra(se):
    s, e = se
    hq = []
    heapq.heappush(hq, (0, s))
    price = [float('inf')] * (N + 1)
    price[s] = 0
    while hq:
        p, v = heapq.heappop(hq)
        if p > price[v]:    continue
        if v == e:
            return price[e]
        for nv, np in bus[v]:
            new_price = p + np
            if new_price < price[nv]:
                price[nv] = new_price
                heapq.heappush(hq, (price[nv], nv))


N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, p = map(int, input().split())
    bus[s].append((e, p))

print(dijkstra(map(int, input().split())))
