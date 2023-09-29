# 31256 KB 48 ms

import sys

N = int(sys.stdin.readline())

board = [[0]*101 for _ in range(101)]

direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

answer = 0

for _ in range(N):
    # x 좌표, y 좌표, 시작 방향, 세대
    x, y, d, g = map(int, sys.stdin.readline().split())
    board[y][x] = 1

    curve = [d]
    length = 1

    for _ in range(g):
        for idx in range(length-1, -1, -1):
            curve.append((curve[idx]+1) % 4)
            length += 1

    for idx in range(length):
        i, j = direction[curve[idx]]
        y, x = y + i, x + j
        board[y][x] = 1

for x in range(101):
    for y in range(101):
        if x+1 > 100 or y+1 > 100:
            continue
        if not board[x][y]:
            continue
        if not board[x+1][y]:
            continue
        if not board[x][y+1]:
            continue
        if not board[x+1][y+1]:
            continue
        answer += 1

print(answer)