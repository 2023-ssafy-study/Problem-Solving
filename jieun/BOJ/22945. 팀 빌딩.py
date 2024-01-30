N = int(input())
x = tuple(map(int, input().split()))

l, r = 0, N - 1
answer = 0
while l + 1 <= r:  # 하나의 팀에는 2명 이상의 개발자 필요
    answer = max(answer, (r - l - 1) * min(x[l], x[r]))
    if x[l] < x[r]:  # 더 작은 능력치를 가진 개발자 제외
        l += 1
    else:
        r -= 1

print(answer)
