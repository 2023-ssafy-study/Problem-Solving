import heapq, sys
input = sys.stdin.readline

N = int(input())
hq = []
heapq.heappush(hq, 0)

classroom = sorted([tuple(map(int, input().split())) for _ in range(N)])
for s, t in classroom:
    ct = heapq.heappop(hq)  # 강의실 중 수업이 제일 일찍 끝난 강의실의 끝난 시각
    if ct > s:  # 같은 강의실에서 진행 불가
        heapq.heappush(hq, ct)
    heapq.heappush(hq, t)

print(len(hq))
