# 240611
# 34088 KB / 64 ms
from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    row, col = map(lambda x: int(x)-1, input().split())
    board[row][col] = 1

L = int(input())
command = {}
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
idx = y = x = 0
time = 0
snake = deque()
for _ in range(L):
    X, C = input().split()
    command[int(X)] = 1 if C == 'D' else -1

snake.append([0, 0])
board[0][0] = 2

while True:
    if command.get(time):
        idx = (idx+command[time]) % 4

    y, x = snake[0][0] + dy[idx], snake[0][1] + dx[idx]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:

        if board[y][x] == 0:
            ny, nx = snake.pop()
            board[ny][nx] = 0

        board[y][x] = 2
        snake.appendleft([y, x])

    else:
        break

    time += 1

print(time+1)


# 34088 KB / 72 ms
from collections import deque

N = int(input()) # 보드 크기
board = [[0] * N for _ in range(N)] #보드판
K = int(input()) # 사과 개수
for _ in range(K):
    row, col = map(lambda x: int(x)-1, input().split())
    board[row][col] = 1

L = int(input()) # 방향 지시 횟수
command = {} # 방향 지시 
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0] # 방향 변환
idx = time = 0 # 방향, 시간
snake = deque() # 뱀
for _ in range(L):
    X, C = input().split()
    command[int(X)] = 1 if C == 'D' else -1

snake.append([0, 0])
board[0][0] = 2

while True:
    if command.get(time):
        idx = (idx+command[time]) % 4

    y, x = snake[0][0] + dy[idx], snake[0][1] + dx[idx]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:

        if board[y][x] == 0:
            ny, nx = snake.pop()
            board[ny][nx] = 0

        board[y][x] = 2
        snake.appendleft([y, x])

    else:
        break

    time += 1

print(time+1)


# 34088 KB / 72 ms
from collections import deque

N = int(input()) # 보드 크기
board = [[0] * N for _ in range(N)] #보드판
K = int(input()) # 사과 개수
for _ in range(K):
    row, col = map(lambda x: int(x)-1, input().split())
    board[row][col] = 1

L = int(input()) # 방향 지시 횟수
command = [0] * 10001 # 방향 지시
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0] # 방향 변환
idx = time = 0 # 방향, 시간
snake = deque() # 뱀
for _ in range(L):
    X, C = input().split()
    command[int(X)] = 1 if C == 'D' else -1

snake.append((0, 0))
board[0][0] = 2

while True:
    if command[time]:
        idx = (idx+command[time]) % 4

    y, x = snake[0][0] + dy[idx], snake[0][1] + dx[idx]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:

        if board[y][x] == 0:
            ny, nx = snake.pop()
            board[ny][nx] = 0

        board[y][x] = 2
        snake.appendleft((y, x))

    else:
        break

    time += 1

print(time+1)
