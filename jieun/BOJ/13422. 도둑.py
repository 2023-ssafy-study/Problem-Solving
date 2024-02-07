T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    money = tuple(map(int, input().split()))
    l, r, answer, steal = 0, M - 1, 0, 0

    for i in range(l, r + 1):
        steal += money[i]

    if N == M:  # 주의!
        if steal < K:
            answer += 1
        print(answer)
        continue

    while l != N:
        if steal < K:
            answer += 1
        steal -= money[l]
        l += 1
        r += 1
        steal += money[r % N]

    print(answer)
