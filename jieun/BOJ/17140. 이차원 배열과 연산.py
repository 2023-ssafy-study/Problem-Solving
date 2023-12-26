def cal_R():  # R 연산
    maxlen = 0
    for i in range(len(A)):
        cnt.clear()
        # 수 정렬하기(0 무시)
        for j in range(len(A[i])):
            if A[i][j] == 0:   continue
            cnt[A[i][j]] = cnt.get(A[i][j], 0) + 1
        A[i] = []
        for n, c in sorted(cnt.items(), key=lambda x: (x[1], x[0])):
            A[i].extend((n, c))
        maxlen = max(maxlen, len(A[i]))

    for i in range(len(A)):  # 행의 크기가 커진 곳에는 0이 채워진다
        for j in range(maxlen - len(A[i])):
            A[i].append(0)


r, c, k = map(int, input().split())
r -= 1
c -= 1
A = [list(map(int, input().split())) for _ in range(3)]
cnt = {}
answer = 0

while answer < 101:
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        print(answer)
        break

    answer += 1
    if len(A) >= len(A[0]):  # R 연산
        cal_R()
    else:  # C 연산
        A = list(map(list, zip(*A)))  # 행과 열을 바꾼다
        cal_R()
        A = list(map(list, zip(*A)))
else:
    print(-1)
