# 240118
# 31120 KB / 3872 ms
N = int(input())
road_info = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_cost = int(1e7)

def dfs(before, level=1, cost=0):
    global min_cost
    if level == N:
        back_to = road_info[before][i]
        if back_to:
            cost += back_to
            if cost < min_cost:
                min_cost = cost
        return

    for j in range(N):
        if not visited[j] and road_info[before][j]:
            visited[j] = True
            dfs(j, level+1, cost+road_info[before][j])
            visited[j] = False

for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False

print(min_cost)


# 31120 KB / 136 ms
N = int(input())
road_info = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_cost = int(1e7)

def dfs(before, level=1, cost=0):
    global min_cost
    if level == N:
        back_to = road_info[before][i]
        if back_to:
            cost += back_to
            if cost < min_cost:
                min_cost = cost
        return

    if min_cost <= cost:
        return

    for j in range(N):
        if not visited[j] and road_info[before][j]:
            visited[j] = True
            dfs(j, level+1, cost+road_info[before][j])
            visited[j] = False

for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False

print(min_cost)



# 31120 KB / 132 ms
N = int(input())
road_info = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_cost = int(1e7)

def dfs(before, level=1, cost=0):
    global min_cost

    if min_cost <= cost:
        return

    if level == N:
        back_to = road_info[before][i]
        if back_to:
            cost += back_to
            if cost < min_cost:
                min_cost = cost
        return

    for j in range(N):
        if not visited[j] and road_info[before][j]:
            visited[j] = True
            dfs(j, level+1, cost+road_info[before][j])
            visited[j] = False

for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False

print(min_cost)



# 31120 KB / 124 ms
N = int(input())
road_info = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_cost = int(1e7)

for i in range(N):
    for j in range(N):
        if road_info[i][j] == 0:
            road_info[i][j] = min_cost


def dfs(before, level=1, cost=0):
    global min_cost

    if min_cost <= cost:
        return

    if level == N:
        cost += road_info[before][i]
        if cost < min_cost:
            min_cost = cost
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            dfs(j, level + 1, cost + road_info[before][j])
            visited[j] = False


for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False

print(min_cost)