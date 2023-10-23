# 231023
# 62724 KB / 320 ms
from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline())
# 강의 목록 : [(시작 시간, 종료 시간), ...]
lecture_list = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
lecture_list.sort()

# 각 강의실별 강의 종료 시간
end_list = [lecture_list[0][1]]
cnt = 1

for start, end in lecture_list[1:]:
    # 가장 종료 시간이 짧은 강의와 현재 강의 시작 시간 비교
    if end_list[0] <= start:
        heappop(end_list)
    else:
        cnt += 1
    heappush(end_list, end)

print(cnt)


# 62724 KB / 284 ms
def cnt_classroom():
    from sys import stdin
    from heapq import heappush, heappop

    N = int(stdin.readline())
    lecture_list = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
    lecture_list.sort()

    end_list = [lecture_list[0][1]]
    cnt = 1

    for start, end in lecture_list[1:]:
        if end_list[0] <= start:
            heappop(end_list)
        else:
            cnt += 1
        heappush(end_list, end)

    return cnt

print(cnt_classroom())