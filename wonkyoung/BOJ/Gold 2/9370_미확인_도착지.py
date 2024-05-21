# 240521
# 47284 KB / 296 ms
def dijkstra():
    n, m, t = map(int, new_input().split())
    s, g, h = map(int, new_input().split())
    link_info = [[] for _ in range(n + 1)]
    limit = 5.1e7
    min_cost = [[limit] * (n+1) for _ in range(3)]
    for i in range(m):
        a, b, d = map(int, new_input().split())
        link_info[a].append((d, b, i))
        link_info[b].append((d, a, i))

    last = set(int(new_input()) for _ in range(t))
    candidate = set()
    start_list = [s, g, h]
    for i in range(3):
        heap = [(0, start_list[i])]
        min_cost[i][start_list[i]] = 0
        visited = [False] * (m+1)

        while heap:
            cost, now = heappop(heap)

            if cost > min_cost[i][now]:
                continue

            for new_cost, new, j in link_info[now]:
                total_cost = cost + new_cost
                if total_cost <= min_cost[i][new] and not visited[j]:
                    visited[j] = True
                    heappush(heap, (total_cost, new))
                    min_cost[i][new] = total_cost

    for num in last:
        # s -> g -> h -> num
        case1 = min_cost[0][g] + min_cost[1][h] + min_cost[2][num]
        if case1 == min_cost[0][num]:
            candidate.add(num)
            continue
        # s -> h -> g -> num
        case2 = min_cost[0][h] + min_cost[1][num] + min_cost[2][g]
        if case2 == min_cost[0][num]:
            candidate.add(num)

    return sorted(candidate)


from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    print(*dijkstra())

'''
1
6 7 3
1 4 5
1 2 1
2 4 2
2 3 2
3 5 3
4 5 3
5 6 4
2 6 9
5
3
6

# 5 6
'''

'''
1
5 5 2
1 2 3
1 4 3
4 5 3
1 2 2
2 3 2
3 5 2
3
5

# 3 5
'''
