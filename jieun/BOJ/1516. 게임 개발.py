from collections import deque


def topology_sort():
    while dq:
        v = dq.popleft()
        result[v] += time[v]  # 선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간
        for nv in graph[v]:
            indegree[nv] -= 1
            result[nv] = max(result[v], result[nv])  # nv의 선수건물 짓는데 걸리는 시간으로 갱신
            if indegree[nv] == 0:
                dq.append(nv)
    print(*result[1:], sep='\n')


N = int(input())
graph = [[] for _ in range(N + 1)]  # 건물 i을 지은 후 지을 수 있는 건물
time = [0]  # 각 건물을 짓는데 걸리는 시간
result = [0] * (N + 1)  # 각 건물이 완성되기까지 걸리는 최소 시간
indegree = [-1] * (N + 1)  # 진입차수
dq = deque()
for i in range(1, N + 1):
    t, *pre = map(int, input().split())
    time.append(t)
    pre.pop()
    indegree[i] = len(pre)  # 진입차수 저장
    if indegree[i] == 0:
        dq.append(i)
    for p in pre:
        graph[p].append(i)

topology_sort()  # 위상정렬(a가 충족되어야 b할 수 있다. DAG(사이클 없는 그래프)에서만 실행 가능)
