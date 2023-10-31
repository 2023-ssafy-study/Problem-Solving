# 231031
def solution(distance, rocks, n):

    rocks.sort()
    start, end = 1, distance

    while start <= end:
        min_gap = (start + end) // 2
        before = cnt = 0
        for rock in rocks:
            gap = rock - before
            if gap < min_gap:
                cnt += 1
            else:
                before = rock
        if distance - before < min_gap:
            cnt += 1

        if cnt > n:
            end = min_gap - 1
        else:
            start = min_gap + 1

    return end