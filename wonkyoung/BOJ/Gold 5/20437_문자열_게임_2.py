# 240202
# 31120 KB / 280 ms
T = int(input())
for _ in range(T):
    word = input()
    K = int(input())
    check = {}
    N = len(word)
    min_len, max_len = N+1, 0
    for i in range(N):
        alp = word[i]
        if check.get(alp):
            check[alp].append(i)
        else:
            check[alp] = [i]

    for alp in check:
        length = len(check[alp])
        if length >= K:
            end = K-1
            for start in range(length-K+1):
                dif = check[alp][end] - check[alp][start] + 1
                if dif > max_len:
                    max_len = dif
                if dif < min_len:
                    min_len = dif
                end += 1

    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)



# 31120 KB / 268 ms
T = int(input())
for _ in range(T):
    word = input()
    K = int(input())
    check = {}
    N = len(word)
    min_len, max_len = N+1, 0
    for i in range(N):
        alp = word[i]
        if check.get(alp):
            check[alp].append(i)
        else:
            check[alp] = [i]

    for alp in check:
        length, end = len(check[alp]), K-1
        for start in range(length-K+1):
            dif = check[alp][end] - check[alp][start] + 1
            if dif > max_len:
                max_len = dif
            if dif < min_len:
                min_len = dif
            end += 1

    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)


# 31120 KB / 156 ms
def find_min_max_len(word, K):
    check = {}
    N = len(word)
    min_len, max_len = N + 1, 0

    for i in range(N):
        alp = word[i]
        if check.get(alp):
            check[alp].append(i)
        else:
            check[alp] = [i]

    for alp in check:
        length, end = len(check[alp]), K - 1
        for start in range(length - K + 1):
            dif = check[alp][end] - check[alp][start] + 1
            if dif > max_len:
                max_len = dif
            if dif < min_len:
                min_len = dif
            end += 1

    if max_len == 0:
        return -1

    return f'{min_len} {max_len}'


T = int(input())
for _ in range(T):
    word = input()
    K = int(input())
    print(find_min_max_len(word, K))




# 31120 KB / 156 ms
def find_min_max_len(word, K):
    check = {}
    N = min_len = len(word)
    max_len = -1

    for i in range(N):
        alp = word[i]
        if check.get(alp):
            check[alp].append(i)
        else:
            check[alp] = [i]

    for alp in check:
        length, end = len(check[alp]), K - 1
        for start in range(length - K + 1):
            dif = check[alp][end] - check[alp][start] + 1
            if dif > max_len:
                max_len = dif
            if dif < min_len:
                min_len = dif
            end += 1

    if max_len == -1:
        return -1

    return f'{min_len} {max_len}'


T = int(input())
for _ in range(T):
    word = input()
    K = int(input())
    print(find_min_max_len(word, K))