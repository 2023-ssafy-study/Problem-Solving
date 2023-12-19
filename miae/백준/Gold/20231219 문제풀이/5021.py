N, M = map(int, input().split())
king = input()
memo = {}

for _ in range(N):
    c, d, m = map(str, input().split())
    memo[c] = [d, m]

def dfs(target):
    global cnt
    # 왕족일때
    if target == king:
        return 1
    # 왕족이 아닌 부모일 때
    if target not in memo:
        return 0
    return (dfs(memo[target][0]) * 0.5) + (dfs(memo[target][1]) * 0.5)
ans = 0
ans_name = ''
for i in range(M):
    target = input()
    ret = dfs(target)
    if ans < ret:
        ans = ret
        ans_name = target
print(ans_name)

