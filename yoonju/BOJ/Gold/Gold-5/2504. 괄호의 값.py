# 31120 KB 40 ms

import sys

strings = list(sys.stdin.readline().rstrip())

stack = []
answer = 0
temp_value = 1

for index in range(len(strings)):
    if strings[index] == '(':
        temp_value *= 2
        stack.append(strings[index])
    elif strings[index] == '[':
        temp_value *= 3
        stack.append(strings[index])
    elif strings[index] == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        if strings[index-1] == '(':
            answer += temp_value
        temp_value //= 2
        stack.pop()
    elif strings[index] == ']':
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        if strings[index-1] == '[':
            answer += temp_value
        temp_value //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)