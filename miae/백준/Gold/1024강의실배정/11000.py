from heapq import heappush, heappop
N = int(input())
lst = [] # 시작점을 봐줄 리스트
for _ in range(N):
    s, t = map(int, input().split())
    lst.append((s, t))
# 시작점 기준 정렬
lst.sort()

h = [lst[0][1]] # 끝점을 봐줄 힙
for i in range(1, N):
    if lst[i][0] >= h[0]:
        heappop(h)
    heappush(h, lst[i][1])
print(len(h))