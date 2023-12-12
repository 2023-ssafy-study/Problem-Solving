def dfs(depth, r, c, prob):
    global answer, visited
    if (r, c) in visited or prob == 0:
        return
    if depth == N:
        answer += prob
        return
    visited.add((r, c))
    dfs(depth + 1, r, c + 1, prob * dirs[0])  # 동
    dfs(depth + 1, r, c - 1, prob * dirs[1])  # 서
    dfs(depth + 1, r + 1, c, prob * dirs[2])  # 남
    dfs(depth + 1, r - 1, c, prob * dirs[3])  # 북
    visited.remove((r, c))


N, *dirs = map(int, input().split())
dirs = tuple(map(lambda p: p * 0.01, dirs))
answer = 0
visited = set()
dfs(0, 0, 0, 1)
print(answer)
