# 34288 KB 2888ms

import sys
from collections import deque

# 90도 회전
def rotate_board(l):
    limit = 2**l
    temp = [[0]*(length) for _ in range(length)]

    for x in range(0, length, limit):
        for y in range(0, length, limit):
            for i in range(limit):
                for j in range(limit):
                    temp[x+j][y+limit-i-1] = board[x+i][y+j]
    return temp

# 얼음 녹이기
def check_melt():
    melt = []

    for x in range(length):
        for y in range(length):
            count = 0
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = x+i, y+j
                if 0 > dx or dx >= length or 0 > dy or dy >= length:
                    continue
                if board[dx][dy]:
                    count += 1
            # 얼음이 있는 칸 3개 이상과 인접해있지 않으면 녹음
            if board[x][y] and count < 3:
                melt.append((x, y))

    for x, y in melt:
        board[x][y] -= 1

def bfs(x, y):
    q = deque([(x, y)])
    check[x][y] = 1
    count = 1

    while q:
        nx, ny = q.popleft()
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = nx + i, ny + j
            if 0 > dx or dx >= length or 0 > dy or dy >= length:
                continue
            if not board[dx][dy]:
                continue
            if check[dx][dy]:
                continue
            check[dx][dy] = 1
            count += 1
            q.append((dx, dy))

    return count

N, Q = map(int, input().split())

length = 2**N

board = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]

QList = list(map(int, sys.stdin.readline().split()))

check = [[0] * length for _ in range(length)]

all_amount = 0
max_count = 0

for L in QList:

    board = rotate_board(L)
    check_melt()

# 남아 있는 얼음 구하기
for x in range(length):
    for y in range(length):
        if board[x][y]:
            all_amount += board[x][y]
            if not check[x][y]:
                res_count = bfs(x, y)
                max_count = max(max_count, res_count)

print(all_amount)
print(max_count)