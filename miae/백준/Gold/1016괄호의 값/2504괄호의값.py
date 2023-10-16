'''
(()[[]])([])
stack을 통해 올바른 괄호인지 확인
조건에 맞도록 temp에 값 추가
'''
b = list(input())
stack = []
temp = 1
ans = 0
for i in range(len(b)):
    if b[i] == '(':
        stack.append(b[i])
        temp *= 2
        #print(stack, temp, ans)

    elif b[i] == '[':
        stack.append(b[i])
        temp *= 3
        #print(stack, temp, ans)

    elif b[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        elif stack[-1] == '(':
            stack.pop()
            if b[i-1] == '(':
                ans += temp
            temp //= 2
            #print(stack, temp, ans)

    elif b[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        elif stack[-1] == '[':
            stack.pop()
            if b[i - 1] == '[':
                ans += temp
            temp //= 3
            #print(stack, temp, ans)

if stack:
    ans = 0
print(ans)