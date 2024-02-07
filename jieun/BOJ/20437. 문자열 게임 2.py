from collections import defaultdict as dd

T = int(input())
for _ in range(T):
    w = input()
    K = int(input())

    char = dd(list)
    for i in range(len(w)):
        char[w[i]].append(i)

    over_k = dd(list)
    for key, val in char.items():
        if len(val) >= K:
            over_k[key] = val
    if not over_k:
        print(-1)
        continue

    min_w, max_w = len(w), 0
    for idx_l in over_k.values():
        for i in range(len(idx_l) - K + 1):
            length = idx_l[i + K - 1] - idx_l[i] + 1
            min_w = min(min_w, length)
            max_w = max(max_w, length)

    print(min_w, max_w)
