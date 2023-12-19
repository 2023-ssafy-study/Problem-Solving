# 231219
# 33164 KB / 904 ms
from sys import stdin
new_input = stdin.readline

N, R = map(int, new_input().split())
city_list = list(set(new_input().split()))
length = len(city_list)
cities = {city_list[i]: i for i in range(length)}
limit = int(2e7)
table1 = [[limit] * length for i in range(length)]
table2 = [[limit] * length for i in range(length)]

M = int(new_input())
path = new_input().split()
K = int(new_input())
info = []
for _ in range(K):
    type_of, start, end, cost = new_input().split()
    cost = int(cost)
    start_i, end_i = cities[start], cities[end]
    info.append((type_of, start_i, end_i, cost))
    value = table1[start_i][end_i]
    if value > cost:
        table1[start_i][end_i] = cost
        table1[end_i][start_i] = cost

for k in range(length):
    for i in range(length):
        if table1[i][k] < limit:
            for j in range(i+1, length):
                if table1[k][j] < limit:
                    table1[i][j] = min(table1[i][j], table1[i][k] + table1[k][j])
                    table1[j][i] = min(table1[i][j], table1[i][k] + table1[k][j])

total_cost = 0
for i in range(M-1):
    start_i, end_i = cities[path[i]], cities[path[i+1]]
    total_cost += table1[start_i][end_i]

if total_cost <= R:
    print('No')
else:
    for i in range(K):
        type_of, start_i, end_i, cost = info[i]
        if type_of.startswith('ITX') or type_of == 'Mugunghwa':
            table2[start_i][end_i] = 0
            table2[end_i][start_i] = 0
        elif type_of.endswith('Train'):
            value, half = table2[start_i][end_i], cost/2
            if value > half:
                table2[start_i][end_i] = half
                table2[end_i][start_i] = half
        else:
            value = table2[start_i][end_i]
            if value > cost:
                table2[start_i][end_i] = cost
                table2[end_i][start_i] = cost

    for k in range(length):
        for i in range(length):
            if table2[i][k] < limit:
                for j in range(i+1, length):
                    if table2[k][j] < limit:
                        table2[i][j] = min(table2[i][j], table2[i][k] + table2[k][j])
                        table2[j][i] = min(table2[i][j], table2[i][k] + table2[k][j])

    new_cost = R
    for i in range(M - 1):
        start_i, end_i = cities[path[i]], cities[path[i + 1]]
        new_cost += table2[start_i][end_i]

    if new_cost < total_cost:
        print('Yes')
    else:
        print('No')
