from heapq import heappop, heappush


def solution(jobs):
    hq = []  # now에 실행할 수 있는 작업들
    now, cnt, answer = 0, 0, 0
    bef = -1  # 이전 요청의 작업 시작 시간

    while cnt != len(jobs):
        for req, time in jobs:
            if bef < req <= now:  # 이전 작업의 실행 시간 사이에 요청이 들어온 작업들을 hq에 push
                heappush(hq, (time, req))

        if hq:
            time, req = heappop(hq)
            bef = now
            now += time
            answer += now - req
            cnt += 1
        else:
            now += 1

    return answer // len(jobs)
