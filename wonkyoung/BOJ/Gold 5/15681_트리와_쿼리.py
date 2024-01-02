# 240102
from sys import stdin
from collections import deque
from heapq import heapify, heappop, heappush

new_input = stdin.readline
N, R, Q = map(int, new_input().split())
node_info = [[] for _ in range(N+1)]
for _ in range(N-1): # 연결 관계 저장
    node1, node2 = map(int, new_input().split())
    node_info[node1].append(node2)
    node_info[node2].append(node1)

# 각 노드별 부모 파악
q = deque()
q.append((R, 0))
visited = [False] * (N+1)
visited[R] = True
parent, subtree = [0] * (N+1), [1] * (N+1)
heap = []
max_level = 0

while q:
    root, level = q.popleft()
    level += 1
    i = 0
    child = node_info[root]
    while i < len(child):
        node = child[i]
        if not visited[node]:
            visited[node] = True
            q.append((node, level))
            i += 1
            parent[node] = root
        else:
            node_info[root].pop(i)

    heap.append((-level+1, root))

# 단말 노드에서부터 올라가며 서브트리에 속한 노드 개수 세기
heapify(heap)
visited = [False] * (N+1)
while True:
    level, node = heappop(heap)
    if not visited[node]:
        visited[node] = True
        for i in node_info[node]:
            subtree[node] += subtree[i]
        if level == 0:
            break
        root = parent[node]
        heappush(heap, (level+1, root))


for _ in range(Q):
    new_root = int(new_input())
    print(subtree[new_root])



