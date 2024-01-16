# M개의 휴게소를 설치했을 때, 휴게소가 없는 구간의 최댓값을 target으로 만들 수 있는지 확인
def isPossible(target):
    build = 0  # 설치해야하는 휴게소의 개수
    for i in range(1, N + 2):
        gap = loc[i] - loc[i - 1]  # 휴게소가 없는 구간
        if gap > target:
            build += (gap - 1) // target  # 현재 설치되어 있는 곳은 제외
        if build > M:
            return False
    return True


N, M, L = map(int, input().split())

loc = [0]
if N:   loc.extend(sorted(map(int, input().split())))
loc.append(L)

l, r, answer = 1, L - 1, 0
while l <= r:
    m = (l + r) // 2
    if isPossible(m):
        r = m - 1
        answer = m
    else:
        l = m + 1
print(answer)
