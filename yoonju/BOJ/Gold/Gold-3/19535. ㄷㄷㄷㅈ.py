import sys
import math

N = int(sys.stdin.readline())

graph = [[] for _ in range(N)]
edges = []

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
    edges.append([u-1, v-1])

D_count, G_count = 0, 0

# D 개수 구하기
for u, v in edges:
    D_count += (len(graph[u]) - 1)*(len(graph[v]) - 1)

# G 개수 구하기
for i in range(N):
    if len(graph[i]) >= 3:
        G_count += math.comb(len(graph[i]), 3)

if D_count > G_count*3:
    print('D')
elif D_count < G_count*3:
    print('G')
else:
    print('DUDUDUNGA')