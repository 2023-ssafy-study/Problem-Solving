# 240123
# 33240 KB / 48 ms
from math import sqrt
N = int(input())
position_list = [list(map(int, input().split())) for _ in range(N)]
limit = 2e7

def square(a): return a*a # 제곱

def distance(x1, y1, x2, y2): return sqrt(square(x1-x2) + square(y1-y2)) # 거리

distance_list = [[0]*N for _ in range(N)] # 각 점 사이 거리
visited = [[0] * N for _ in range(1 << N - 1)] # 방문 여부에 따른 최소 비용

for i in range(N):
    x1, y1 = position_list[i]
    for j in range(i+1, N):
        x2, y2 = position_list[j]
        value = distance(x1, y1, x2, y2)
        distance_list[i][j] = value
        distance_list[j][i] = value
def tsp(now=0, idx=0):
    if visited[idx][now]:
        return visited[idx][now]

    if idx == (1 << (N-1)) - 1:
        return distance_list[now][0] if distance_list[now][0] else limit

    min_cost = limit
    for i in range(1, N):
        if idx & (1 << i - 1):
            continue

        cost = tsp(i, idx | (1 << (i - 1))) + distance_list[now][i]

        if min_cost > cost:
            min_cost = cost

    if min_cost < limit:
        visited[idx][now] = min_cost

    return min_cost


min_cost = tsp()
print(min_cost if min_cost < limit else -1)
