# 155560 KB 1704 ms

import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

count = {}

answer = [-1]*N

stack = []

for a in arr:
    if a not in count:
        count[a] = 0
    count[a] += 1

for index in range(N-1, -1, -1):
    while stack:
        if count[arr[index]] < count[stack[-1]]:
            answer[index] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(arr[index])

print(*answer)