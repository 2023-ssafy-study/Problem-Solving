# 231002
C, N = map(int, input().split())
max_val = 1e6
cost_list = [max_val] * 10001
limit = C
for _ in range(N):
    cost, customer = map(int, input().split())
    cost_list[customer] = min(cost, cost_list[customer])
    if C%customer and limit < C+customer:
        limit = C+customer

    for i in range(customer+1, limit+1):
        cost_list[i] = min(cost_list[i], cost_list[i-customer]+cost)

print(min(cost_list[C:]))


#
C, N = map(int, input().split())
max_val = 1e6
cost_list = [max_val] * 2001
limit = C
for _ in range(N):
    cost, customer = map(int, input().split())
    cost_list[customer] = min(cost, cost_list[customer])
    if C%customer and limit < C+customer:
        limit = C+customer

    for i in range(customer+1, limit+1):
        cost_list[i] = min(cost_list[i], cost_list[i-customer]+cost)

print(min(cost_list[C:]))

#
C, N = map(int, input().split())
max_val = 1e6
cost_list = [max_val] * 1101
limit = C
for _ in range(N):
    cost, customer = map(int, input().split())
    cost_list[customer] = min(cost, cost_list[customer])
    if C%customer and limit < C+customer:
        limit = C+customer

    for i in range(customer+1, limit+1):
        cost_list[i] = min(cost_list[i], cost_list[i-customer]+cost)

print(min(cost_list[C:]))


#
C, N = map(int, input().split())
max_val = 1e6
cost_list = [max_val] * 1101
limit = C
info = []
for _ in range(N):
    cost, customer = map(int, input().split())
    info.append((cost/customer, cost, customer))

info.sort()
before_ratio = 0
for i in range(N):
    ratio, cost, customer = info[i]
    if ratio != before_ratio:
        cost_list[customer] = min(cost, cost_list[customer])
        if C%customer and limit < C+customer:
            limit = C+customer

        for i in range(customer+1, limit+1):
            cost_list[i] = min(cost_list[i], cost_list[i-customer]+cost)

print(min(cost_list[C:]))


#
C, N = map(int, input().split())
max_val = 1e6
cost_list = [max_val] * 1101
limit = C
info = []
for _ in range(N):
    cost, customer = map(int, input().split())
    info.append((cost/customer, cost, customer))

info.sort()
before_ratio = 0
for i in range(N):
    ratio, cost, customer = info[i]
    if ratio != before_ratio:
        cost_list[customer] = min(cost, cost_list[customer])
        if C%customer and limit < C+customer:
            limit = C+customer

        for i in range(customer+1, limit+1):
            cost_list[i] = min(cost_list[i], cost_list[i-customer]+cost)

print(min(cost_list[C:limit+1]))


#
def find_min_cost():
    C, N = map(int, input().split())
    max_val = 1e6
    cost_list = [max_val] * 1101
    limit = C
    info = []
    for _ in range(N):
        cost, customer = map(int, input().split())
        info.append((cost/customer, cost, customer))

    info.sort()
    before_ratio = 0
    for i in range(N):
        ratio, cost, customer = info[i]
        if ratio != before_ratio:
            cost_list[customer] = min(cost, cost_list[customer])
            if C%customer and limit < C+customer:
                limit = C+customer

            for i in range(customer+1, limit+1):
                cost_list[i] = min(cost_list[i], cost_list[i-customer]+cost)

    return min(cost_list[C:limit+1])

print(find_min_cost())
