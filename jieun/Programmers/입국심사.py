def solution(n, times):
    answer = max(times) * n  # 최대: 모두 시간이 오래 걸리는 심사를 받을 경우
    times.sort(reverse=True)

    def isPossible(sec):
        tmp_people = n
        for time in times:
            tmp_people -= sec // time  # sec//time: sec초 이내에 해결할 수 있는 최대 사람 수
            if tmp_people <= 0:
                return True
        return False

    def bs(left, right):
        nonlocal answer
        if left > right:
            return
        mid = (left + right) // 2
        if isPossible(mid):  # mid초 내에 해결 가능?
            answer = min(answer, mid)
            return bs(0, mid - 1)
        else:
            return bs(mid + 1, right)

    bs(0, max(times) * n)

    return answer
