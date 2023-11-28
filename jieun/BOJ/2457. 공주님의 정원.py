import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    bm, bd, wm, wd = map(int, input().split())
    if wm < 3 or bm == 12:    continue
    arr.append((bm * 100 + bd, wm * 100 + wd))
arr.sort()
end_date = 301  # 정원의 마지막 꽃이 지는 날짜
cnt = 0

while arr:
    if end_date >= 1201 or end_date < arr[0][0]: break

    tmp_end_date = -1
    for _ in range(len(arr)):
        if arr[0][0] <= end_date:
            if tmp_end_date <= arr[0][1]:
                tmp_end_date = arr[0][1]
            del arr[0]
        else:
            break

    end_date = tmp_end_date
    cnt += 1

print(0 if end_date < 1201 else cnt)
