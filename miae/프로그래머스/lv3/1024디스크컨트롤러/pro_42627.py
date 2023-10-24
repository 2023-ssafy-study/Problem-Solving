1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
from heapq import heappop, heappush
def solution(jobs):
    l = len(jobs)
    cnt = 0 # 작업한 수
    answer = 0
    # 이전에 완료한 종료시점(시작해야할 시점), 현재시점
    start = -1
    now = 0
    heap = []
    while jobs:
        for call, work in jobs:
            # 작업종료했던 시점부터 지금까지 요청한 것 중에 작업시간 짧은 것부터 넣어줌
            if start < call <= now:
                heappush(heap, (work, call))

        if heap:
            cur = heappop(heap)
            # 시작해야할 시점
            start = now
            # 현재시점 (작업완료한시점)
            now += cur[0]
            # 요청부터 작업종료까지 시간
            answer += (now - cur[1])
            # 작업 완료
            jobs.remove([cur[1], cur[0]])
        else:
            now += 1 # 작업이 없어 쉼
    answer = answer // l
    return answer