N = int(input())
lst = []
arr = [0] * 367  # 365일, 각 열의 값 = 행의 길이
end = 0 # N개 일정 중 가장 마지막 일정
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        arr[i] += 1
    end = max(end, e)
ci = 0 # 직사각형 최대행 (상단부터 배치되기 때문에 시작점 필요X)
sj = 0 # 직사각형 시작열
ans = 0
for j in range(1, end+2):
    if arr[j] == 0:
       ans += (j - sj) * ci
       ci, sj = 0, 0
    else:
        if sj == 0:
            sj = j
        ci = max(ci, arr[j])
print(ans)