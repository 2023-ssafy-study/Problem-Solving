T = int(input())
def inspect():
    for j in range(W):
        start = film[0][j]
        cnt = 0
        for i in range(D):
            if start == film[i][j]:
               cnt += 1
            else:
                start = film[i][j]
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            # K개 연속된 셀이 없음
            return False
    return True

def dfs(cnt, start_idx):
    global ans
    # 모든 행을 다칠하고도 안될 때
    if cnt > D:
        return
    # 검사
    if inspect():
        ans = min(cnt, ans)
        return
    if cnt >= ans:
        return
    for i in range(start_idx, D):
        lst = [0] * W
        # 원래 거
        for j in range(W):
            lst[j] = film[i][j]
        # 0으로 투입
        for j in range(W):
            film[i][j] = 0
        dfs(cnt+1, i+1)
        # 1로 투입
        for j in range(W):
            film[i][j] = 1
        dfs(cnt+1, i+1)
        # 백트래킹
        for j in range(W):
            film[i][j] = lst[j]

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    ans = int(1e9)
    dfs(0, 0)
    print(f'#{tc} {ans}')