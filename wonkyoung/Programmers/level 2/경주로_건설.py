# 240528
def solution(board):

    from collections import deque

    def push_to_q(y, x, idx, cost):
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = cost + 1 if idx == i or idx == -1 else cost + 6
                if visited[ny][nx][i] > new_cost:
                    q.append((ny, nx, i, new_cost))
                    visited[ny][nx][i] = new_cost

    min_cost, n = 25 * 25 * 5, len(board)
    dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]
    visited = [[[min_cost] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()

    push_to_q(0, 0, -1, 0)
    visited[0][0] = [0] * 4

    while q:
        y, x, i, cost = q.popleft()
        if y == n - 1 and x == n - 1:
            continue

        push_to_q(y, x, i, cost)

    return min(*visited[-1][-1]) * 100

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.11ms, 10.1MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (1.55ms, 10.3MB)
테스트 7 〉	통과 (2.26ms, 10.3MB)
테스트 8 〉	통과 (1.49ms, 10.3MB)
테스트 9 〉	통과 (0.76ms, 10.1MB)
테스트 10 〉	통과 (1.66ms, 10.3MB)
테스트 11 〉	통과 (32.35ms, 10.2MB)
테스트 12 〉	통과 (5.44ms, 10.3MB)
테스트 13 〉	통과 (0.39ms, 10.1MB)
테스트 14 〉	통과 (0.87ms, 10.4MB)
테스트 15 〉	통과 (2.20ms, 10.3MB)
테스트 16 〉	통과 (4.14ms, 10.3MB)
테스트 17 〉	통과 (10.99ms, 10.2MB)
테스트 18 〉	통과 (25.02ms, 10MB)
테스트 19 〉	통과 (21.16ms, 10.3MB)
테스트 20 〉	통과 (3.68ms, 10.3MB)
테스트 21 〉	통과 (1.58ms, 10.2MB)
테스트 22 〉	통과 (0.13ms, 10.4MB)
테스트 23 〉	통과 (0.12ms, 10.3MB)
테스트 24 〉	통과 (0.23ms, 10.4MB)
테스트 25 〉	통과 (0.07ms, 10.4MB)
'''


#
def solution(board):
    # 0 비어 있음, 1 벽
    from collections import deque

    def push_to_q(y, x, idx, cost):
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = cost + 1 if idx == i or idx == -1 else cost + 6
                if visited[ny][nx][i] > new_cost:
                    q.append((ny, nx, i, new_cost))
                    visited[ny][nx][i] = new_cost

    min_cost, n = 3750, len(board)
    dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]
    visited = [[[min_cost] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()

    push_to_q(0, 0, -1, 0)
    visited[0][0] = [0] * 4

    while q:
        y, x, i, cost = q.popleft()
        if y == n - 1 and x == n - 1:
            continue

        push_to_q(y, x, i, cost)

    return min(*visited[-1][-1]) * 100


'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.1MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (2.09ms, 10.4MB)
테스트 7 〉	통과 (1.53ms, 10.3MB)
테스트 8 〉	통과 (2.64ms, 10.2MB)
테스트 9 〉	통과 (0.77ms, 10.3MB)
테스트 10 〉	통과 (1.94ms, 10.4MB)
테스트 11 〉	통과 (37.04ms, 10.3MB)
테스트 12 〉	통과 (5.48ms, 10.4MB)
테스트 13 〉	통과 (0.41ms, 10.3MB)
테스트 14 〉	통과 (0.83ms, 10.3MB)
테스트 15 〉	통과 (3.02ms, 10.3MB)
테스트 16 〉	통과 (5.18ms, 10.3MB)
테스트 17 〉	통과 (7.29ms, 10.2MB)
테스트 18 〉	통과 (15.10ms, 10.1MB)
테스트 19 〉	통과 (21.53ms, 10.1MB)
테스트 20 〉	통과 (4.28ms, 10.4MB)
테스트 21 〉	통과 (1.72ms, 10.3MB)
테스트 22 〉	통과 (0.23ms, 10.3MB)
테스트 23 〉	통과 (0.12ms, 10.3MB)
테스트 24 〉	통과 (0.14ms, 10.4MB)
테스트 25 〉	통과 (0.07ms, 10.3MB)

'''


#
def solution(board):
    from collections import deque

    # q에 값 넣기
    def push_to_q(y, x, idx, cost):
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = cost + 1 if idx == i or idx == -1 else cost + 6
                if visited[ny][nx][i] > new_cost:
                    q.append((ny, nx, i, new_cost))
                    visited[ny][nx][i] = new_cost

    # 초기화 & bfs
    def find_min():

        push_to_q(0, 0, -1, 0)
        visited[0][0] = [0] * 4

        while q:
            y, x, i, cost = q.popleft()
            if y == n - 1 and x == n - 1:
                continue

            push_to_q(y, x, i, cost)

        return min(*visited[-1][-1]) * 100

    # 변수 선언
    min_cost, n = 3750, len(board)
    dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]
    visited = [[[min_cost] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()

    return find_min()

'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.10ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.4MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (1.55ms, 10.4MB)
테스트 7 〉	통과 (2.58ms, 10.3MB)
테스트 8 〉	통과 (2.78ms, 10MB)
테스트 9 〉	통과 (1.58ms, 10.4MB)
테스트 10 〉	통과 (2.95ms, 10.4MB)
테스트 11 〉	통과 (53.45ms, 10.2MB)
테스트 12 〉	통과 (11.18ms, 10.2MB)
테스트 13 〉	통과 (0.40ms, 10.1MB)
테스트 14 〉	통과 (0.92ms, 10.3MB)
테스트 15 〉	통과 (2.73ms, 10.3MB)
테스트 16 〉	통과 (8.52ms, 10.1MB)
테스트 17 〉	통과 (8.03ms, 10.1MB)
테스트 18 〉	통과 (19.31ms, 10.1MB)
테스트 19 〉	통과 (37.76ms, 10.3MB)
테스트 20 〉	통과 (4.21ms, 10.3MB)
테스트 21 〉	통과 (1.61ms, 10.2MB)
테스트 22 〉	통과 (0.25ms, 10.3MB)
테스트 23 〉	통과 (0.19ms, 10.3MB)
테스트 24 〉	통과 (0.13ms, 10.3MB)
테스트 25 〉	통과 (0.08ms, 10.4MB)
'''

#
# q에 값 넣기
def push_to_q(y, x, idx, cost, board, visited, dy, dx, n, q):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
            new_cost = cost + 1 if idx == i or idx == -1 else cost + 6
            if visited[ny][nx][i] > new_cost:
                q.append((ny, nx, i, new_cost))
                visited[ny][nx][i] = new_cost


def solution(board):
    from collections import deque

    # 변수 선언
    min_cost, n = 3750, len(board)
    dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]
    visited = [[[min_cost] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()

    # 초기화 & bfs
    push_to_q(0, 0, -1, 0, board, visited, dy, dx, n, q)
    visited[0][0] = [0] * 4

    while q:
        y, x, i, cost = q.popleft()
        if y == n - 1 and x == n - 1:
            continue

        push_to_q(y, x, i, cost, board, visited, dy, dx, n, q)

    return min(*visited[-1][-1]) * 100


'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (1.55ms, 10.2MB)
테스트 7 〉	통과 (1.51ms, 10.1MB)
테스트 8 〉	통과 (1.65ms, 10.3MB)
테스트 9 〉	통과 (0.78ms, 10.1MB)
테스트 10 〉	통과 (1.74ms, 10.3MB)
테스트 11 〉	통과 (28.00ms, 10MB)
테스트 12 〉	통과 (5.42ms, 10.1MB)
테스트 13 〉	통과 (0.41ms, 10.3MB)
테스트 14 〉	통과 (0.53ms, 10.2MB)
테스트 15 〉	통과 (2.27ms, 10.3MB)
테스트 16 〉	통과 (3.96ms, 10.3MB)
테스트 17 〉	통과 (12.88ms, 10.1MB)
테스트 18 〉	통과 (14.79ms, 10.2MB)
테스트 19 〉	통과 (21.49ms, 10.1MB)
테스트 20 〉	통과 (2.09ms, 10.1MB)
테스트 21 〉	통과 (1.56ms, 10.2MB)
테스트 22 〉	통과 (0.13ms, 10.4MB)
테스트 23 〉	통과 (0.12ms, 10.3MB)
테스트 24 〉	통과 (0.13ms, 10.3MB)
테스트 25 〉	통과 (0.07ms, 10.2MB)
'''