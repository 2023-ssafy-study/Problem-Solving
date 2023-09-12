answer = 0
def my_dfs(n, numbers, target, value):
    global answer
    N = len(numbers)
    if (n == N and target == value):
        answer += 1
        return
    if n == N:
        return
    my_dfs(n+1, numbers, target, value+numbers[n])
    my_dfs(n+1, numbers, target, value-numbers[n])
        
def solution(numbers, target):
    global answer
    my_dfs(0, numbers, target, 0)
    return answer