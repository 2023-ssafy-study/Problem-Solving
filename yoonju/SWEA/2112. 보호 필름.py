# 딕셔너리를 활용한 코드
# 101,860 kb / 4,231 ms

T = int(input())
 
for t in range(1, T+1):
    def check_performance(board, k, change):
        for y in range(len(board[0])):
            count = 0
            prev = board[0][y]
            if 0 in change:
                prev = change[0]
            for x in range(1, len(board)):
                now = board[x][y]
                if x in change:
                    now = change[x]
                if prev == now:
                    count += 1
                else:
                    count = 0
                if count == k-1:
                    break
                prev = now
            if count < K-1:
                return False
        return True
 
    def dfs(level, idx, change):
        global answer
        if level >= answer:
            return
 
        if check_performance(board, K, change):
            answer = min(answer, level)
            return
 
        for i in range(idx+1, D):
            if i in change:
                continue
            for type in [0, 1]:
                change[i] = type
                dfs(level+1, i, change)
                del change[i]
    """
    D = 보호 필름 두께
    W = 가로 크기
    K = 합격 기준
    """
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    answer = D
 
    dfs(0, -1, {})
 
    print(f'#{t} {answer}')


# board를 변경하는 코드
# 68,604 kb / 1,860 ms

T = int(input())

for t in range(1, T+1):
    def check_performance(board, k):
        for y in range(len(board[0])):
            count = 0
            prev = board[0][y]
            for x in range(1, len(board)):
                now = board[x][y]
                if prev == now:
                    count += 1
                else:
                    count = 0
                if count == k-1:
                    break
                prev = now
            if count < K-1:
                return False
        return True

    def dfs(level, idx):
        global answer
        if level >= answer:
            return

        if check_performance(board, K):
            answer = min(answer, level)
            return

        for i in range(idx+1, D):
            origin = [0]*W
            for y in range(W):
                origin[y] = board[i][y]
            for type in [0, 1]:
                board[i] = [type]*W
                dfs(level+1, i)
            board[i] = origin

    """
    D = 보호 필름 두께
    W = 가로 크기
    K = 합격 기준
    """
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    answer = D

    dfs(0, -1)

    print(f'#{t} {answer}')