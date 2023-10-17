# 109172 KB 632 ms

import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
answer = [0]*N
prev_towers = []

for index in range(N-1, -1, -1):
    while prev_towers:
        if prev_towers[-1][1] < towers[index]:
            answer[prev_towers[-1][0]] = index+1
            prev_towers.pop()
        else:
            break
    prev_towers.append((index, towers[index]))

print(*answer)