# 240520
# 37548 KB / 1016 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

n, m = to_int()
limit = 3e5
next_position = [['-'] * (n+1) for _ in range(n+1)]
min_time = [[limit] * (n+1) for _ in range(n+1)]
link_info = [[] for _ in range(n+1)]

for i in range(1, n+1):
    min_time[i][i] = 0

for _ in range(m):
    a, b, time = to_int()
    link_info[a].append((time, b))
    link_info[b].append((time, a))
    min_time[a][b] = time
    min_time[b][a] = time

for i in range(1, n+1):
    heap = []
    for time, next_node in link_info[i]:
        heappush(heap, (time, next_node, next_node))
        next_position[i][next_node] = str(next_node)

    while heap:
        time, next_node, answer_node = heappop(heap)
        if min_time[i][next_node] < time:
            continue

        for new_time, new_node in link_info[next_node]:
            total_time = time + new_time
            if total_time < min_time[i][new_node]:
                min_time[i][new_node] = total_time
                heappush(heap, (total_time, new_node, answer_node))
                next_position[i][new_node] = str(answer_node)


for i in range(1, n+1):
    print(' '.join(next_position[i][1:]))


# 37576 KB / 960 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

n, m = to_int()
limit = 3e5
next_position = [['-'] * n for _ in range(n)]
min_time = [[limit] * n for _ in range(n)]
link_info = [[] for _ in range(n)]

for i in range(n):
    min_time[i][i] = 0

for _ in range(m):
    a, b, time = to_int()
    a -= 1
    b -= 1
    link_info[a].append((time, b))
    link_info[b].append((time, a))
    min_time[a][b] = time
    min_time[b][a] = time

for i in range(n):
    heap = []
    for time, next_node in link_info[i]:
        heappush(heap, (time, next_node, next_node+1))
        next_position[i][next_node] = str(next_node+1)

    while heap:
        time, next_node, answer_node = heappop(heap)
        if min_time[i][next_node] < time:
            continue

        for new_time, new_node in link_info[next_node]:
            total_time = time + new_time
            if total_time < min_time[i][new_node]:
                min_time[i][new_node] = total_time
                heappush(heap, (total_time, new_node, answer_node))
                next_position[i][new_node] = str(answer_node)


for i in range(n):
    print(' '.join(next_position[i]))