import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline


def dfs(v):
    global stack, answer
    if visited[v]:
        if v in stack:
            while stack:
                answer -= 1
                if stack.pop() == v:
                    break
        return
    visited[v] = True
    stack.append(v)
    dfs(sel[v])


T = int(input())
for _ in range(T):
    n = int(input())
    sel = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    answer = n
    for s in range(1, n + 1):
        if visited[s]:  continue
        stack = []
        dfs(s)
    print(answer)
