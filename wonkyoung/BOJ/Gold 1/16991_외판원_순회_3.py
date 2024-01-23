# 240123
# 47576 KB / 808 ms
from math import sqrt
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
limit = 2e4

def square(a): return a * a

def calc_dist(x1, y1, x2, y2): return sqrt(square(x1-x2)+square(y1-y2))

visited = [[0] * N for _ in range(1 << N - 1)]
distance_list = [[0]*N for _ in range(N)]

for i in range(N):
    x1, y1 = city[i]
    for j in range(i+1, N):
        x2, y2 = city[j]
        value = calc_dist(x1, y1, x2, y2)
        distance_list[i][j] = value
        distance_list[j][i] = value

def tsp(now=0, idx=0):
    if visited[idx][now]:
        return visited[idx][now]

    if idx == (1 << (N-1)) - 1:
        return distance_list[now][0] if distance_list[now][0] else limit

    min_cost = limit
    for i in range(1, N):
        if idx & (1 << i-1):
            continue

        cost = tsp(i, idx | (1 << i-1)) + distance_list[now][i]
        if cost < min_cost:
            min_cost = cost

    if min_cost < limit:
        visited[idx][now] = min_cost
    return min_cost


print(tsp())
