#231001
# 카드를 정확히 N개 구매했을 때 최대 금액 찾기
# 1 <= N <= 1000
N = int(input())
price_of_cards = [0] + list(map(int, input().split())) # 카드팩 가격
cost = price_of_cards[:] # 구매한 카드 개수(인덱스)별 금액(값)
for i in range(2, N+1):
    for j in range(1, i):
        new_cost = cost[i-j] + cost[j]
        if new_cost > cost[i]:
            cost[i] = new_cost

print(cost[N])


# 반복 횟수 줄이기
N = int(input())
price_of_cards = [0] + list(map(int, input().split())) # 카드팩 가격
cost = price_of_cards[:] # 구매한 카드 개수(인덱스)별 금액(값)
for i in range(2, N+1):
    for j in range(1, i//2+1):
        new_cost = cost[i-j] + cost[j]
        if new_cost > cost[i]:
            cost[i] = new_cost

print(cost[N])


# 배열 하나 줄이기
N = int(input())
cost = [0] + list(map(int, input().split())) # 구매한 카드 개수(인덱스)별 금액(값) (초기값 = 카드팩 가격)
for i in range(2, N+1):
    for j in range(1, i//2+1):
        new_cost = cost[i-j] + cost[j]
        if new_cost > cost[i]:
            cost[i] = new_cost

print(cost[N])


# max_cost 생성
N = int(input())
cost = [0] + list(map(int, input().split())) # 구매한 카드 개수(인덱스)별 금액(값) (초기값 = 카드팩 가격)
for i in range(2, N+1):
    max_cost = cost[i]
    for j in range(1, i//2+1):
        new_cost = cost[i-j] + cost[j]
        if new_cost > max_cost:
            max_cost = new_cost
    cost[i] = max_cost

print(cost[N])

# 배열 하나 줄이기
N = int(input())
# 구매한 카드 개수(인덱스)별 금액(값) (초기값 = 카드팩 가격)
cost = [0]
cost.extend(map(int, input().split()))
for i in range(2, N+1):
    for j in range(1, i//2+1):
        new_cost = cost[i-j] + cost[j]
        if new_cost > cost[i]:
            cost[i] = new_cost

print(cost[N])


#
def find_max_cost():
    N = int(input())
    cost_of_cards = [0] + list(map(int, input().split()))  # 구매한 카드 개수(인덱스)별 금액(값) (초기값 = 카드팩 가격)
    for i in range(2, N + 1):
        for j in range(1, i // 2 + 1):
            new_cost = cost_of_cards[i - j] + cost_of_cards[j]
            if new_cost > cost_of_cards[i]:
                cost_of_cards[i] = new_cost

    return cost_of_cards[N]

print(find_max_cost())
