N = int(input())
men = sorted(map(int, input().split()))
women = sorted(map(int, input().split()))

answer = 0
l, r = 0, N - 1
while 0 <= r and l < N:
    m, w = men[l], women[r]
    if (m < 0 < w) or (m > 0 > w):  # 큰 여자&작은 남자 or 큰 남자&작은 여자
        if m + w < 0:  # 작은 사람과 춤 추고 싶은 사람이 더 큰 키를 가지고 있음
            answer += 1
            l += 1
            r -= 1
        else:
            r -= 1
    elif m < 0 and w < 0:
        l += 1
    elif 0 < m and 0 < w:
        r -= 1

print(answer)
