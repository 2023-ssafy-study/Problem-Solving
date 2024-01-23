# 240123
# 45452 KB / 884 ms
N = int(input())
cost_table = [list(map(int, input().split())) for _ in range(N)]
max_cost = int(2e7)
visited = [[0]*N for _ in range(1 << N - 1)]

def tsp(now=0, idx=0):

    if visited[idx][now]:
        return visited[idx][now]

    if idx == (1 << (N - 1)) - 1:
        return cost_table[now][0] if cost_table[now][0] else max_cost

    min_cost = max_cost
    for i in range(1, N):
        if not cost_table[now][i]:
            continue
        if idx & (1 << i - 1):
            continue
        cost = cost_table[now][i] + tsp(i, idx | (1 << (i - 1)))
        if min_cost > cost:
            min_cost = cost

    visited[idx][now] = min_cost

    return min_cost


print(tsp())
