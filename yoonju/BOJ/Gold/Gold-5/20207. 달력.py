# 31256 KB 76 ms

import sys

N = int(sys.stdin.readline())

days = [0]*366

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    for idx in range(start, end+1):
        days[idx] += 1

cnt = 0
depth = 0
answer = 0

for idx in range(1, 366):
    if not days[idx]:
        if cnt or depth:
            answer += cnt*depth
            cnt = 0
            depth = 0
        continue
    cnt += 1
    depth = max(depth, days[idx])

if cnt or depth:
    answer += cnt*depth

print(answer)