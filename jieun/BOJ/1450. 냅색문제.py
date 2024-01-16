from itertools import combinations


def bs(e1):  # 조건에 충족하는 idx 중 가장 큰 값 반환
    l, r = 0, len(s2) - 1
    while l <= r:
        m = (l + r) // 2
        if s2[m] + e1 <= C:
            l = m + 1
        else:
            r = m - 1
    return l


N, C = map(int, input().split())
weights = sorted(map(int, input().split()))

# MITM
# 반으로 나눈다
w1 = weights[:N // 2]
w2 = weights[N // 2:]
# 부분 집합의 합 구하기
s1, s2 = [], []
for i in range(len(w1) + 1):
    for c in combinations(w1, i):
        s1.append(sum(c))
for i in range(len(w2) + 1):
    for c in combinations(w2, i):
        s2.append(sum(c))
# 이분탐색을 위해 s2 정렬
s2.sort()

answer = 0
for e1 in s1:
    if C - e1 < 0:  continue
    answer += bs(e1)

print(answer)
