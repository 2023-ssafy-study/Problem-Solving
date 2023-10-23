#231019
#231020
'''
정확성  테스트
테스트 1 〉	통과 (0.98ms, 10.1MB)
테스트 2 〉	통과 (0.85ms, 10.3MB)
테스트 3 〉	통과 (0.74ms, 10MB)
테스트 4 〉	통과 (0.40ms, 10.2MB)
테스트 5 〉	통과 (0.54ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.60ms, 10.2MB)
테스트 8 〉	통과 (0.26ms, 10.2MB)
테스트 9 〉	통과 (0.18ms, 10.2MB)
테스트 10 〉	통과 (0.63ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''

def solution(jobs): # job : [작업이 요청되는 시점, 작업의 소요시간]
    from heapq import heapify, heappush, heappop
    length = len(jobs)
    heapify(jobs)

    candidates = [] # candidate : [작업 소요 시간, 요청되는 시점]
    total_duration = now = 0 # 요청부터 종료까지 걸린 총 시간 ,현재 시간

    while jobs or candidates:
        # 현재 시간보다 일찍 요청한 경우
        while jobs and now > jobs[0][0]:
            start, duration = heappop(jobs)
            heappush(candidates, (duration, start))

        # 처리할 일이 없는 경우 -> 가장 먼저 온 작업 처리
        if not candidates:
            start, duration = heappop(jobs)
            total_duration += duration
            now = start + duration
        else:
            # 처리할 일이 있는 경우 -> 가장 소요 시간이 짧은 작업 처리
            duration, start = heappop(candidates)
            total_duration += (now - start) + duration
            now = now + duration

    return int(total_duration/length)


'''
정확성  테스트
테스트 1 〉	통과 (0.98ms, 10.4MB)
테스트 2 〉	통과 (0.46ms, 10MB)
테스트 3 〉	통과 (0.68ms, 10.2MB)
테스트 4 〉	통과 (0.40ms, 10.1MB)
테스트 5 〉	통과 (0.84ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.63ms, 10.1MB)
테스트 8 〉	통과 (0.40ms, 10.1MB)
테스트 9 〉	통과 (0.17ms, 10.2MB)
테스트 10 〉	통과 (0.90ms, 9.99MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10MB)
'''

#
def solution(jobs):  # job : [작업이 요청되는 시점, 작업의 소요시간]
    from heapq import heapify, heappush, heappop
    length = len(jobs)
    heapify(jobs)

    candidates = []  # candidate : [작업 소요 시간, 요청되는 시점]
    total_duration = now = 0  # 요청부터 종료까지 걸린 총 시간 ,현재 시간

    for _ in range(length):
        # 현재 시간보다 일찍 요청한 경우
        while jobs and now > jobs[0][0]:
            start, duration = heappop(jobs)
            heappush(candidates, (duration, start))

        # 처리할 일이 없는 경우 -> 가장 먼저 온 작업 처리
        if not candidates:
            start, duration = heappop(jobs)
            total_duration += duration
            now = start + duration
        else:
            # 처리할 일이 있는 경우 -> 가장 소요 시간이 짧은 작업 처리
            duration, start = heappop(candidates)
            total_duration += (now - start) + duration
            now = now + duration

    return int(total_duration / length)



#
'''
정확성  테스트
테스트 1 〉	통과 (0.95ms, 10.3MB)
테스트 2 〉	통과 (0.45ms, 10.2MB)
테스트 3 〉	통과 (0.48ms, 10.3MB)
테스트 4 〉	통과 (0.37ms, 10.3MB)
테스트 5 〉	통과 (0.89ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.69ms, 10.3MB)
테스트 8 〉	통과 (0.25ms, 10.2MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)
테스트 10 〉	통과 (0.56ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''
'''
정확성  테스트
테스트 1 〉	통과 (0.78ms, 10.2MB)
테스트 2 〉	통과 (0.84ms, 10.2MB)
테스트 3 〉	통과 (0.38ms, 10.1MB)
테스트 4 〉	통과 (0.73ms, 10.2MB)
테스트 5 〉	통과 (0.50ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.35ms, 10.2MB)
테스트 8 〉	통과 (0.24ms, 10.1MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)
테스트 10 〉	통과 (0.53ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10MB)
테스트 14 〉	통과 (0.01ms, 10MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''
def solution(jobs):  # job : [작업이 요청되는 시점, 작업의 소요시간]
    from heapq import heappush, heappop
    length = len(jobs)
    jobs.sort()

    candidates = []  # candidate : [작업 소요 시간, 요청되는 시점]
    total_duration = now = 0  # 요청부터 종료까지 걸린 총 시간 ,현재 시간
    i = 0

    for _ in range(length):
        # 현재 시간보다 일찍 요청한 경우
        while i < length and now > jobs[i][0]:
            start, duration = jobs[i]
            heappush(candidates, (duration, start))
            i += 1

        # 처리할 일이 없는 경우 -> 가장 먼저 온 작업 처리
        if not candidates:
            start, duration = jobs[i]
            i += 1
            total_duration += duration
            now = start + duration
        else:
            # 처리할 일이 있는 경우 -> 가장 소요 시간이 짧은 작업 처리
            duration, start = heappop(candidates)
            total_duration += (now - start) + duration
            now = now + duration

    return int(total_duration / length)