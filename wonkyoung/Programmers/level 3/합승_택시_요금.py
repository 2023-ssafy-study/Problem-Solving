# 240430
def solution(n, s, a, b, fares):
    # 지점 개수, 출발지점, A 도착지점, B 도착지점, 예상 택시 요금
    # 합승 X : s -> a + s -> b
    # 합승 : s -> m + m -> a + m -> b

    limit = int(2e7) + 1
    path_table = [[limit] * (n + 1) for _ in range(n + 1)]

    for c, d, f in fares:
        path_table[c][d] = f
        path_table[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if i != k:
                i_to_k = path_table[i][k]
                path_table[i][i] = 0
                for j in range(i + 1, n + 1):
                    if j != k:
                        through_k = i_to_k + path_table[k][j]
                        if through_k < path_table[i][j]:
                            path_table[i][j] = path_table[j][i] = through_k

    # 합승 X : s -> a + s -> b
    min_total = path_table[s][a] + path_table[s][b]

    # 합승 : s -> m + m -> a + m -> b
    for k in range(1, n + 1):
        if s != k:
            total = path_table[s][k] + path_table[k][a] + path_table[k][b]
            if total < min_total:
                min_total = total

    return min_total

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.10ms, 10.2MB)
테스트 5 〉	통과 (0.15ms, 10.3MB)
테스트 6 〉	통과 (0.24ms, 10.4MB)
테스트 7 〉	통과 (0.29ms, 10.2MB)
테스트 8 〉	통과 (0.59ms, 10.4MB)
테스트 9 〉	통과 (0.66ms, 10.3MB)
테스트 10 〉	통과 (0.63ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (64.55ms, 10.2MB)
테스트 2 〉	통과 (218.98ms, 10.9MB)
테스트 3 〉	통과 (500.27ms, 11MB)
테스트 4 〉	통과 (498.60ms, 10.9MB)
테스트 5 〉	통과 (499.40ms, 10.9MB)
테스트 6 〉	통과 (498.30ms, 10.7MB)
테스트 7 〉	통과 (519.77ms, 13.4MB)
테스트 8 〉	통과 (521.58ms, 13.4MB)
테스트 9 〉	통과 (537.70ms, 12.9MB)
테스트 10 〉	통과 (534.04ms, 13MB)
테스트 11 〉	통과 (542.81ms, 12.9MB)
테스트 12 〉	통과 (519.60ms, 12.1MB)
테스트 13 〉	통과 (519.90ms, 12.2MB)
테스트 14 〉	통과 (520.26ms, 12.1MB)
테스트 15 〉	통과 (521.81ms, 12.2MB)
테스트 16 〉	통과 (496.45ms, 10.6MB)
테스트 17 〉	통과 (496.86ms, 10.7MB)
테스트 18 〉	통과 (499.74ms, 10.7MB)
테스트 19 〉	통과 (505.96ms, 11MB)
테스트 20 〉	통과 (509.29ms, 11.1MB)
테스트 21 〉	통과 (510.38ms, 11.2MB)
테스트 22 〉	통과 (522.88ms, 12.1MB)
테스트 23 〉	통과 (526.35ms, 12.1MB)
테스트 24 〉	통과 (524.37ms, 12.1MB)
테스트 25 〉	통과 (493.13ms, 10.6MB)
테스트 26 〉	통과 (492.70ms, 10.7MB)
테스트 27 〉	통과 (469.08ms, 10.4MB)
테스트 28 〉	통과 (470.52ms, 10.4MB)
테스트 29 〉	통과 (63.79ms, 10.4MB)
테스트 30 〉	통과 (64.56ms, 10.3MB)
'''


#
def minus_one(num):
    return num - 1


def solution(n, s, a, b, fares):
    # 지점 개수, 출발지점, A 도착지점, B 도착지점, 예상 택시 요금
    limit = int(2e7) + 1
    s, a, b = map(minus_one, [s, a, b])
    path_table = [[limit] * n for _ in range(n)]

    for c, d, f in fares:
        c, d = map(minus_one, [c, d])
        path_table[c][d] = path_table[d][c] = f

    for k in range(n):
        for i in range(n):
            if i != k:
                i_to_k = path_table[i][k]
                path_table[i][i] = 0
                for j in range(i + 1, n):
                    if j != k:
                        through_k = i_to_k + path_table[k][j]
                        if through_k < path_table[i][j]:
                            path_table[i][j] = path_table[j][i] = through_k

    # 합승 X : s -> a + s -> b
    min_total = path_table[s][a] + path_table[s][b]

    # 합승 : s -> m + m -> a + m -> b
    for k in range(n):
        if s != k:
            total = path_table[s][k] + path_table[k][a] + path_table[k][b]
            if total < min_total:
                min_total = total

    return min_total

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.14ms, 10.2MB)
테스트 5 〉	통과 (0.16ms, 10.3MB)
테스트 6 〉	통과 (0.24ms, 10.3MB)
테스트 7 〉	통과 (0.17ms, 10.3MB)
테스트 8 〉	통과 (0.35ms, 10.5MB)
테스트 9 〉	통과 (0.50ms, 10.3MB)
테스트 10 〉	통과 (0.64ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (65.61ms, 10.2MB)
테스트 2 〉	통과 (218.78ms, 10.9MB)
테스트 3 〉	통과 (498.43ms, 10.9MB)
테스트 4 〉	통과 (497.12ms, 10.9MB)
테스트 5 〉	통과 (498.09ms, 10.7MB)
테스트 6 〉	통과 (497.10ms, 10.9MB)
테스트 7 〉	통과 (530.34ms, 13.3MB)
테스트 8 〉	통과 (525.04ms, 13.3MB)
테스트 9 〉	통과 (543.05ms, 12.9MB)
테스트 10 〉	통과 (547.13ms, 12.9MB)
테스트 11 〉	통과 (550.65ms, 13MB)
테스트 12 〉	통과 (520.01ms, 12.1MB)
테스트 13 〉	통과 (522.62ms, 12.2MB)
테스트 14 〉	통과 (522.74ms, 12.2MB)
테스트 15 〉	통과 (519.89ms, 12.1MB)
테스트 16 〉	통과 (495.33ms, 10.8MB)
테스트 17 〉	통과 (497.55ms, 10.7MB)
테스트 18 〉	통과 (497.22ms, 10.7MB)
테스트 19 〉	통과 (507.80ms, 10.9MB)
테스트 20 〉	통과 (509.53ms, 11.3MB)
테스트 21 〉	통과 (509.04ms, 11.2MB)
테스트 22 〉	통과 (521.24ms, 12.2MB)
테스트 23 〉	통과 (523.67ms, 12.2MB)
테스트 24 〉	통과 (519.30ms, 12.2MB)
테스트 25 〉	통과 (500.57ms, 10.6MB)
테스트 26 〉	통과 (495.42ms, 10.6MB)
테스트 27 〉	통과 (470.84ms, 10.4MB)
테스트 28 〉	통과 (477.67ms, 10.5MB)
테스트 29 〉	통과 (65.18ms, 10.4MB)
테스트 30 〉	통과 (63.83ms, 10.3MB)
'''


#
def minus_one(num):
    return num - 1


def solution(n, s, a, b, fares):
    # 지점 개수, 출발지점, A 도착지점, B 도착지점, 예상 택시 요금
    limit = (int(1e5) * n) + 1
    s, a, b = map(minus_one, [s, a, b])
    path_table = [[limit] * n for _ in range(n)]

    for c, d, f in fares:
        c, d = map(minus_one, [c, d])
        path_table[c][d] = path_table[d][c] = f

    for k in range(n):
        for i in range(n):
            if i != k:
                i_to_k = path_table[i][k]
                path_table[i][i] = 0
                for j in range(i + 1, n):
                    if j != k:
                        through_k = i_to_k + path_table[k][j]
                        if through_k < path_table[i][j]:
                            path_table[i][j] = path_table[j][i] = through_k

    # 합승 X : s -> a + s -> b
    min_total = path_table[s][a] + path_table[s][b]

    # 합승 : s -> m + m -> a + m -> b
    for k in range(n):
        if s != k:
            total = path_table[s][k] + path_table[k][a] + path_table[k][b]
            if total < min_total:
                min_total = total

    return min_total


'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.28ms, 10.3MB)
테스트 6 〉	통과 (0.24ms, 10.3MB)
테스트 7 〉	통과 (0.17ms, 10.3MB)
테스트 8 〉	통과 (0.35ms, 10.3MB)
테스트 9 〉	통과 (0.49ms, 10.3MB)
테스트 10 〉	통과 (1.20ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (65.07ms, 10.4MB)
테스트 2 〉	통과 (217.61ms, 10.8MB)
테스트 3 〉	통과 (500.57ms, 11MB)
테스트 4 〉	통과 (507.88ms, 10.9MB)
테스트 5 〉	통과 (501.53ms, 10.7MB)
테스트 6 〉	통과 (497.32ms, 10.9MB)
테스트 7 〉	통과 (523.41ms, 13.3MB)
테스트 8 〉	통과 (525.34ms, 13.4MB)
테스트 9 〉	통과 (539.58ms, 13MB)
테스트 10 〉	통과 (543.96ms, 13MB)
테스트 11 〉	통과 (540.34ms, 13MB)
테스트 12 〉	통과 (542.32ms, 12.1MB)
테스트 13 〉	통과 (520.75ms, 12.2MB)
테스트 14 〉	통과 (519.85ms, 12.2MB)
테스트 15 〉	통과 (523.17ms, 12.3MB)
테스트 16 〉	통과 (497.06ms, 11MB)
테스트 17 〉	통과 (498.06ms, 10.7MB)
테스트 18 〉	통과 (497.12ms, 10.8MB)
테스트 19 〉	통과 (504.53ms, 11MB)
테스트 20 〉	통과 (509.39ms, 11.3MB)
테스트 21 〉	통과 (510.20ms, 11.1MB)
테스트 22 〉	통과 (521.67ms, 12.2MB)
테스트 23 〉	통과 (521.02ms, 12.2MB)
테스트 24 〉	통과 (522.41ms, 12.1MB)
테스트 25 〉	통과 (492.71ms, 10.7MB)
테스트 26 〉	통과 (492.66ms, 10.6MB)
테스트 27 〉	통과 (467.85ms, 10.4MB)
테스트 28 〉	통과 (472.98ms, 10.6MB)
테스트 29 〉	통과 (63.90ms, 10.3MB)
테스트 30 〉	통과 (63.80ms, 10.2MB)
'''