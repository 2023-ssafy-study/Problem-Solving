import heapq, sys
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x == 0:
        print(-heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, -x)
