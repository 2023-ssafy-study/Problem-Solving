# 240709
# 229084 KB / 4648 ms
def to_int():
    return map(int, input().split())

N, K = to_int()
items = []

for i in range(N):
    w, v = to_int()
    if w <= K:
        items.append((w, v))

M = len(items)
max_val = 0

check = [[0] * (K+1) for i in range(M+1)]
for i in range(1, M+1):
    w, v = items[i-1]
    for nw in range(1, K+1):
        if nw < w:
            check[i][nw] = check[i-1][nw]
        else:
            check[i][nw] = max(check[i-1][nw], check[i-1][nw-w] + v)

print(check[-1][-1])



# 229084 KB / 4404 ms
def to_int():
    return map(int, input().split())

N, K = to_int()
items = []

for i in range(N):
    w, v = to_int()
    if w <= K:
        items.append((w, v))

M = len(items)

check = [[0] * (K+1) for i in range(M+1)]
for i in range(1, M+1):
    w, v = items[i-1]
    for nw in range(1, w):
        check[i][nw] = check[i-1][nw]

    for nw in range(w, K+1):
        check[i][nw] = max(check[i-1][nw], check[i-1][nw-w] + v)

print(check[-1][-1])



# 39604 KB / 3324 ms
def to_int():
    return map(int, input().split())

N, K = to_int()
items = []

for i in range(N):
    w, v = to_int()
    if w <= K:
        items.append((w, v))

M = len(items)

check = [0] * (K+1)
for i in range(1, M+1):
    w, v = items[i-1]
    temp = [0] * (K+1)
    for nw in range(1, w):
        temp[nw] = check[nw]

    for nw in range(w, K+1):
        temp[nw] = max(check[nw], check[nw-w] + v)

    check = temp[:]

print(check[-1])



# 39604 KB / 3364 ms
def to_int():
    return map(int, input().split())

N, K = to_int()
items = []

for i in range(N):
    w, v = to_int()
    if w <= K:
        items.append((w, v))

M = len(items)
items.sort(reverse=True)

check = [0] * (K+1)
for i in range(1, M+1):
    w, v = items[i-1]
    temp = [0] * (K+1)

    for nw in range(w, K+1):
        temp[nw] = max(check[nw], check[nw-w] + v)

    check = temp[:]

print(check[-1])


