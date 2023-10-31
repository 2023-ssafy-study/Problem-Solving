def bs(l, r):
    global min_sum, answer
    if l > r:   return

    m = (l + r) // 2
    tmp_sum = liq[std] + liq[m]
    if abs(tmp_sum) <= min_sum:
        answer = (liq[std], liq[m])
        min_sum = abs(tmp_sum)

    if tmp_sum == 0:
        return
    elif tmp_sum < 0:
        bs(m + 1, r)
    else:
        bs(l, m - 1)


N = int(input())
liq = sorted(map(int, input().split()))
answer = ()
min_sum = 2000000001
for i in range(N):
    std = i
    bs(i + 1, N - 1)
print(*answer)
