# 40380 KB / 220 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
inorder = [0] * (N+1)
next_problems = [[] for _ in range(N+1)]
heap, result = [], []

for _ in range(M):
    A, B = to_int()
    next_problems[A].append(B)
    inorder[B] += 1

for i in range(1, N+1):
    if inorder[i] == 0:
        heappush(heap, i)

while heap:
    num = heappop(heap)
    result.append(num)
    for i in next_problems[num]:
        inorder[i] -= 1
        if inorder[i] == 0:
            heappush(heap, i)

print(*result)


# 40380 KB / 216 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
inorder = [0] * (N+1)
next_problems = [[] for _ in range(N+1)]
heap, result = [], []

for _ in range(M):
    A, B = to_int()
    next_problems[A].append(B)
    inorder[B] += 1

for i in range(1, N+1):
    if inorder[i] == 0:
        heap.append(i)

while heap:
    num = heappop(heap)
    result.append(num)
    for i in next_problems[num]:
        inorder[i] -= 1
        if inorder[i] == 0:
            heappush(heap, i)

print(*result)
