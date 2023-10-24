from heapq import heappop, heappush
N = int(input())
h = []
for _ in range(N):
    h.append(int(input()))
h.sort()

ans = 0
if len(h) == 1:
    print(ans)
else:
    while h:
        a = heappop(h)
        if not h:
            break
        b = heappop(h)
        ans += (a+b)
        heappush(h, a+b)
    print(ans)