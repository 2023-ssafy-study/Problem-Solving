import sys
sys.setrecursionlimit(int(1e6))

def dfs(i, cycle):
    global ans, visit
    visit[i] = True
    cycle.append(i)

    if visit[lst[i]] == True:
        if lst[i] in cycle:
             ans -= len(cycle[cycle.index(lst[i]):])
        return
    else:
        dfs(lst[i], cycle)

T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    visit = [False] * (N+1)
    ans = N
    for i in range(1, N+1):
        if visit[i]:
            continue
        dfs(i, [])
    print(ans)