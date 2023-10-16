'''
오른쪽에서 왼쪽으로, 자신의 값보다 크거나 같은수를 찾는 문제
(반복문, stack)
첫번쨰 값은 무조건 0
반복문을 통해 탐색
    stack 마지막 값과 현재값 비교
    stack 마지막 값이 현재값보다 작으면
        수신되지 못하는 값이므로 작은것들은 빼준다. => pop
        stack이 비어있으면
            0
        있으면
            stack 마지막값이 수신된 탑
    크거나 같으면
        수신된 레이저 탑임
'''
N = int(input())
lst = list(map(int, input().split()))
stack = [(lst[0], 1)]
ans = [0] * N
for i in range(1, N):
    top, idx = lst[i], i+1
    if stack[-1][0] < top:
        while stack and stack[-1][0] < top:
            stack.pop()
        if not stack:
            ans[i] = 0
        else:
            ans[i] = stack[-1][1]
    else:
        ans[i] = stack[-1][1]
    stack.append((top, idx))
print(*ans)