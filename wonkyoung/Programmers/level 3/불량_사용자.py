# 240423
def solution(user_id, banned_id):
    n, m = len(user_id), len(banned_id)
    # 제외 아이디와 매칭되는 아이디 인덱스
    candidate = [[] for _ in range(m)]

    # 제외 아이디별
    for i in range(m):
        target = banned_id[i]
        l = len(target)
        # 모든 아이디
        for j in range(n):
            ref = user_id[j]
            if len(ref) == l:
                # 각 요소 비교
                for k in range(l):
                    if target[k] != ref[k] and target[k] != '*':
                        break
                else:
                    candidate[i].append(j)

    # 아이디 목록을 넣어놓을 set (중복 제거)
    answer_set = set()

    # level: banned_id 인덱스, result: 비트마스킹 이용한 아이디 정보
    def choose_id(level, result):

        if level == m:
            answer_set.add(result)
            return

        for i in candidate[level]:
            if not (result & (1 << i)):
                choose_id(level + 1, result | 1 << i)

    choose_id(0, 0)

    return len(answer_set)

'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (73.41ms, 10.2MB)
테스트 6 〉	통과 (0.64ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
'''


#
def solution(user_id, banned_id):
    n, m = len(user_id), len(banned_id)
    # 제외 아이디와 매칭되는 아이디 인덱스
    candidate = [[] for _ in range(m)]
    # 아이디 목록을 체크할 리스트
    answer_check = [False] * (1 << n)

    # 제외 아이디별
    for i in range(m):
        target = banned_id[i]
        l = len(target)
        # 모든 아이디
        for j in range(n):
            ref = user_id[j]
            if len(ref) == l:
                # 각 요소 비교
                for k in range(l):
                    if target[k] != ref[k] and target[k] != '*':
                        break
                else:
                    candidate[i].append(j)

    # level: banned_id 인덱스, result: 비트마스킹 이용한 아이디 정보
    def choose_id(level, result):

        if level == m:
            answer_check[result] = True
            return

        for i in candidate[level]:
            if not (result & (1 << i)):
                choose_id(level + 1, result | 1 << i)

    choose_id(0, 0)

    return answer_check.count(True)

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (66.08ms, 10.2MB)
테스트 6 〉	통과 (0.65ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
'''