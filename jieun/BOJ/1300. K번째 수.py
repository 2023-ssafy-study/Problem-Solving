N, k = int(input()), int(input())

l, r, answer = 1, k, 0
while l <= r:
    m = (l + r) // 2

    cnt = 0
    for i in range(1, N + 1):
        cnt += min(m // i, N)  # m//i: i열의 m이하인 숫자의 개수

    if cnt >= k:
        r = m - 1
        answer = m
    else:
        l = m + 1

print(answer)
