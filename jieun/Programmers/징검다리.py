def solution(distance, rocks, n):
    rocks.sort()  # 오름차순 정렬
    rocks.append(distance)

    answer = 0
    l, r = 1, distance

    while l <= r:
        m = (l + r) // 2  # 바위 제거해서 최소 거리 m 만들 수 있는지?
        left_rock = 0  # 왼쪽 바위 위치
        cnt = 0  # 제거된 바위의 개수
        for i in range(len(rocks)):
            right_rock = rocks[i]  # 오른쪽 바위 위치
            if right_rock - left_rock < m:  # 간격이 m보다 작으면 오른쪽 바위(right_rock) 제거
                cnt += 1
            else:
                left_rock = right_rock  # 왼쪽 바위 위치를 옮긴다
            if n < cnt:
                break

        if cnt <= n:  # 돌을 더 제거해서 answer을 키울 수 있는가
            answer = m
            l = m + 1
        else:
            r = m - 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))  # 4
