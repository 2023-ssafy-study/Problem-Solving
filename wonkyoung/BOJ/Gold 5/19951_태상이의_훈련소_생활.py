# 240709
# 41932 KB / 272 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
heights = list(to_int())
dif = [0] * (N+1)

for _ in range(M):
    a, b, k = to_int()
    dif[a-1] += k
    dif[b] -= k

for i in range(1, N):
    dif[i] += dif[i-1]

for i in range(N):
    heights[i] += dif[i]

print(*heights)



# 41932 KB / 268 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

N, M = to_int()
heights = list(to_int())
dif = [0] * (N+1)

for _ in range(M):
    a, b, k = to_int()
    dif[a-1] += k
    dif[b] -= k

heights[0] += dif[0]

for i in range(1, N):
    dif[i] += dif[i-1]
    heights[i] += dif[i]

print(*heights)

#
