'''
등장횟수 고려하기 => 자료구조 이용하자 : dict
오른쪽에 있으면서 가장 왼쪽에 있는 수 찾기 => append, pop 활용 : stack
반복문을 n번을 통해 탐색
    현재값과 stack의 마지막값과 비교
    현재값이 stack[-1]의 오등큰수이면:
        stack안의 마지막수부터, 조건에 맞는 값을 찾으면 => pop하면서 저장

stack에 (값,idx)를 같이 저장해서 답을 구할 때 ans[idx] = 현재값 저장
'''
N = int(input())
lst = list(map(int, input().split()))

F = {}
for i in range(N):
    if lst[i] not in F:
        F[lst[i]] = 0
    F[lst[i]] += 1

ans = [-1] * N
stack = [(lst[0], 0)]
for i in range(1, N):
    if F[stack[-1][0]] < F[lst[i]]:
        while stack and F[stack[-1][0]] < F[lst[i]]:
            num, idx = stack.pop()
            ans[idx] = lst[i]
    stack.append((lst[i], i))
print(*ans)