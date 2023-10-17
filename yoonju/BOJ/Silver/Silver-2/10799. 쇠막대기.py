# 32336 KB 64 ms

import sys

sticks = list(sys.stdin.readline().rstrip())
stack = []

answer = 0

for idx in range(len(sticks)):
    if sticks[idx] == '(':
        stack.append(sticks[idx])
    elif sticks[idx] == ')':
        stack.pop()
        if sticks[idx-1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)