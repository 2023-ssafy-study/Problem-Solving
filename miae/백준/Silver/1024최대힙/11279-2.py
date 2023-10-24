from heapq import heappop, heappush
import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline
N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(h, -x)
    else:
        if h:
            cur = heappop(h)
            print(-cur)
        else:
            print(0)
