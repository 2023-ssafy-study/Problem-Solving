'''
1. 각 행의 합 구하기 => sum함수 이용
2. 회전한 맵 만들기 => rotate 구현 필요
    r, c, s 정보를 이용
    왼 -> 오, 아래 -> 위, 오 -> 왼, 아래 -> 위 방향 : 각각 (s * 2)칸이 바뀜
3. 회전 순서 구하기 => 백트래킹 이용
    visit 이용
134680 메모리 712 시간
'''
from copy import deepcopy
def rotate(arr, q):
    new = deepcopy(arr)
    for o in q:
        cr, cc, cs = orders[o][0], orders[o][1], orders[o][2]
        for i in range(cs, -1, -1):
            for k in range(1, 2 * i + 1):
                new[cr - i][cc - i + k] = arr[cr - i][cc - i + k - 1]
            for k in range(1, 2 * i + 1):
                new[cr - i + k][cc + i] = arr[cr - i + k - 1][cc + i]
            for k in range(1, 2 * i + 1):
                new[cr + i][cc + i - k] = arr[cr + i][cc + i - k + 1]
            for k in range(1, 2 * i + 1):
                new[cr + i - k][cc - i] = arr[cr + i - k + 1][cc - i]
        arr = deepcopy(new)
    return new

def solve(cnt):
    global visit, ans, q
    if cnt == K:
        new = rotate(board, q)
        for i in range(N):
            ans = min(ans, sum(new[i]))
        return
    for i in range(K):
        if visit[i] == 1:
            continue
        visit[i] = 1
        # 회전해야함
        #new = rotate(maps, i)
        q.append(i)
        solve(cnt+1)
        q.pop()
        visit[i] = 0

N, M, K = map(int, input().split())
# 초기 배열
board = [list(map(int, input().split())) for _ in range(N)]
# 연산 방법
orders = []
for _ in range(K):
    r, c, s = map(int, input().split())
    orders.append((r-1, c-1, s))
# 연산 순서
visit = [0] * K
q = []
ans = 5001
solve(0)
print(ans)