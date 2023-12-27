# 231227
from sys import stdin
from collections import deque
def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
parent = [0] + list(to_int())
total = [0] * (N+1)

for _ in range(M):
    idx, value = to_int()
    total[idx] += value

q = deque()
visited = [False] * (N+1)

for i in range(2, N+1):
    q.append(parent[i])
    visited[i] = True
    while q:
        j = q.popleft()
        if j == 1:
            break
        total[i] += total[j]
        if visited[j]:
            q.clear()
            break
        q.append(parent[j])

print(*total[1:])
