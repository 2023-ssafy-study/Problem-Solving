# 231023
# 33972 KB / 188 ms
# 개수가 적은 카드 묶음부터 더함
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return int(stdin.readline())

N = to_int()
card_packs = []
total_conf = 0
for _ in range(N):
    heappush(card_packs, to_int())

while len(card_packs) > 1:
    card_pack1 = heappop(card_packs)
    card_pack2 = heappop(card_packs)
    conf = card_pack1+card_pack2
    total_conf += conf
    heappush(card_packs, conf)

print(total_conf)


# 33972 KB / 212 ms
from sys import stdin
from heapq import heappush, heappop

def to_int():
    return int(stdin.readline())

N = to_int()
card_packs = []
total_conf = 0
for _ in range(N):
    heappush(card_packs, to_int())

while len(card_packs) > 1:
    conf = 0
    for _ in range(2):
        conf += heappop(card_packs)
    total_conf += conf
    heappush(card_packs, conf)

print(total_conf)


# 33972 KB / 184 ms
from sys import stdin
from heapq import heapify, heappush, heappop

def to_int():
    return int(stdin.readline())

N = to_int()
card_packs = [to_int() for _ in range(N)]
total_conf = 0
heapify(card_packs)


while len(card_packs) > 1:
    card_pack1 = heappop(card_packs)
    card_pack2 = heappop(card_packs)
    conf = card_pack1+card_pack2
    total_conf += conf
    heappush(card_packs, conf)

print(total_conf)