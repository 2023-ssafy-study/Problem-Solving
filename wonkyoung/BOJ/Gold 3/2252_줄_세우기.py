# 240524
# 28460 KB / 212 ms
from sys import stdin
from collections import deque

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
order_info = [[] for _ in range(N+1)]
inorder = [0] * (N+1)
q = deque()
result = []

for _ in range(M):
    A, B = to_int()
    order_info[A].append(B)
    inorder[B] += 1

for i in range(1, N+1):
    if inorder[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    result.append(num)

    for next_num in order_info[num]:
        inorder[next_num] -= 1
        if inorder[next_num] == 0:
            q.append(next_num)

print(*result)