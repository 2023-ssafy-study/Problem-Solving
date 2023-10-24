import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

answer = 0
while len(cards) > 1:   # 카드 묶음이 하나가 남을 때까지 진행
    # 최소로 비교하기 위해서는 카드 개수가 적은 묶음끼리 비교해야 함 => 힙 사용
    cc = heapq.heappop(cards) + heapq.heappop(cards)
    answer += cc
    heapq.heappush(cards, cc)

print(answer)
