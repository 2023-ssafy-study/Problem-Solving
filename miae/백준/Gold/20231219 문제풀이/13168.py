from collections import deque
from heapq import heappop, heappush
sales = {
    'Subway': 1,
    'Bus': 1,
    'Taxi': 1,
    'Airplane': 1,
    'KTX': 1,
    'S-Train': 0.5,
    'V-Train': 0.5,
    'ITX-Saemaeul': 0,
    'ITX-Cheongchun': 0,
    'Mugunghwa': 0
}

N, R = map(int, input().split())
#
A = list(map(str, input().split()))
M = int(input())
B = list(map(str, input().split()))
K = int(input())
origin_board = [[] for _ in range(N)]
nailo_board = [[] for _ in range(N)]

# 간선정보 입력
for k in range(K):
    t, s, e, c = map(str, input().split())
    s_idx, e_idx, c = A.index(s), A.index(e), float(c)
    origin_board[s_idx].append((e_idx, c))
    origin_board[e_idx].append((s_idx, c))
    nailo_board[s_idx].append((e_idx, float(c*sales[t])))
    nailo_board[e_idx].append((s_idx, float(c*sales[t])))

def dijk(start):
    heap = []
    heap2 = []
    heappush(heap, (0, start))
    heappush(heap2, (0, start))

    dist[start] = 0
    dist2[start] = 0

    while heap:
        cost, cur = heappop(heap)
        if dist[cur] < cost:
            continue
        for n, next_cost in origin_board[cur]:
            next = next_cost + cost
            if next < dist[n]:
                dist[n] = next
                heappush(heap, (next, n))
    while heap2:
        cost, cur = heappop(heap2)
        if dist2[cur] < cost:
            continue
        for n, next_cost in nailo_board[cur]:
            next = next_cost + cost
            if next < dist2[n]:
                dist2[n] = next
                heappush(heap2, (next, n))

origin_c, nailo_c = 0, R
for j in range(1, M):
    start = B[j-1]
    start_idx = A.index(start)
    end = B[j]
    end_idx = A.index(end)
    o, n = int(1e9), int(1e9)
    dist = [int(1e9)] * N
    dist2 = [int(1e9)] * N

    dijk(start_idx)
    origin_c += dist[end_idx]
    nailo_c += dist2[end_idx]

if origin_c > nailo_c:
    print('Yes')
else:
    print('No')