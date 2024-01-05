from heapq import heappush, heappop
from sys import stdin

input = stdin.readline


def dijkstra(graph_t):
    time = [float('inf')] * (N + 1)
    time[0], time[X] = 0, 0
    hq = []
    heappush(hq, (0, X))
    while hq:
        cur_time, pos = heappop(hq)
        if cur_time > time[pos]:    continue
        for next_pos, next_time in graph_t[pos]:
            tmp = cur_time + next_time
            if tmp < time[next_pos]:
                time[next_pos] = tmp
                heappush(hq, (time[next_pos], next_pos))
    return time


N, M, X = map(int, input().split())
answer = 0
graph = [[] for _ in range(N + 1)]  # 정방향, n -> X
rev_graph = [[] for _ in range(N + 1)]  # 역방향, X -> n
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    rev_graph[e].append((s, t))

print(max(map(sum, zip(dijkstra(graph), dijkstra(rev_graph)))))
