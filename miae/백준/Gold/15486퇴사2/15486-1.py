import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * (N+2)
for i in range(1, N+1):
    # 전날값과 현재값 비교
    lst[i] = max(lst[i], lst[i-1])
    # 인풋
    t, p = map(int, input().split())
    # N+1일 내 일을 할 수 있는 것만
    if i+t < N+2:
        # i+t날에 현재값+인풋p 와 i+t날의 값 비교
        lst[i+t] = max(lst[i] + p, lst[i+t])
print(max(lst[N], lst[N+1]))