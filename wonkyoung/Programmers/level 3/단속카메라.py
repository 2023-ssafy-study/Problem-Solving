# 231113
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 9.91MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.79ms, 10.5MB)
테스트 2 〉	통과 (0.47ms, 10.5MB)
테스트 3 〉	통과 (2.14ms, 10.7MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (2.36ms, 10.8MB)
'''
def solution(routes):
    routes.sort(key=lambda route: (route[1], route[0]))
    i = answer = 1
    dot = routes[0][1]
    n = len(routes)
    while i < n:
        start, end = routes[i]
        if dot < start:
            answer += 1
            dot = end
        i += 1

    return answer


#
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 9.97MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.76ms, 10.5MB)
테스트 2 〉	통과 (0.59ms, 10.4MB)
테스트 3 〉	통과 (2.03ms, 10.7MB)
테스트 4 〉	통과 (0.11ms, 10.2MB)
테스트 5 〉	통과 (2.36ms, 10.8MB)
'''
def solution(routes):
    routes.sort(key=lambda route: (route[1], route[0]))
    answer = 1
    dot = routes[0][1]
    n = len(routes)
    for i in range(1, n):
        start, end = routes[i]
        if dot < start:
            answer += 1
            dot = end

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))