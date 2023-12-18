N, R = map(int, input().split())  # 도시의 수, 내일로 티켓의 가격
cities = input().split()
to_idx = {}  # 도시 인덱스 저장
for i in range(N):
    to_idx[cities[i]] = i

M = int(input())  # 여행할 도시의 수
route = []
for city in input().split():
    route.append(to_idx[city])

K = int(input())  # 교통수단의 수
railro_b = [[float('inf')] * N for _ in range(N)]  # 내일로 구매 o
railro_nb = [[float('inf')] * N for _ in range(N)]  # 구매 x
for i in range(N):  # 자기 자신으로 가는 비용 초기화
    railro_b[i][i] = 0
    railro_nb[i][i] = 0
for _ in range(K):
    type, s, e, cost = input().split()
    s, e, cost = to_idx[s], to_idx[e], int(cost)

    railro_nb[s][e] = min(railro_nb[s][e], cost)
    railro_nb[e][s] = min(railro_nb[e][s], cost)

    if type in {'Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun'}:
        railro_b[s][e] = 0
        railro_b[e][s] = 0
    elif type in {'S-Train', 'V-Train'}:
        railro_b[s][e] = min(railro_b[s][e], cost / 2)
        railro_b[e][s] = min(railro_b[s][e], cost / 2)
    else:
        railro_b[s][e] = min(railro_b[s][e], cost)
        railro_b[e][s] = min(railro_b[e][s], cost)

# 플로이드–워셜
for k in range(N):
    for s in range(N):
        for e in range(N):
            railro_b[s][e] = min(railro_b[s][e], railro_b[s][k] + railro_b[k][e])
            railro_nb[s][e] = min(railro_nb[s][e], railro_nb[s][k] + railro_nb[k][e])

cost_b, cost_nb = R, 0  # 내일로 구매 시, 구매하지 않을 시 가격
for i in range(M - 1):
    cost_b += railro_b[route[i]][route[i + 1]]
    cost_nb += railro_nb[route[i]][route[i + 1]]
print('Yes' if cost_b < cost_nb else 'No')
