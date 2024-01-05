from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def dijkstra(r, c):
    AOJ = [[10001] * N for _ in range(M)]  # 알고스팟의 무기 AOJ 사용 횟수
    AOJ[r][c] = 0
    hq = []
    heappush(hq, (AOJ[r][c], r, c))

    while hq:
        cur_aoj, r, c = heappop(hq)
        if r == M - 1 and c == N - 1:
            return AOJ[M - 1][N - 1]
        if AOJ[r][c] < cur_aoj:
            continue
        for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if 0 <= nr < M and 0 <= nc < N:
                # 빈 방은 0, 벽은 1이므로 이전까지 부신 횟수에 더해주면 현재까지 부신 벽 개수
                tmp = cur_aoj + miro[nr][nc]
                if tmp < AOJ[nr][nc]:  # 기존 값보다 작을 때만 갱신, heappush
                    AOJ[nr][nc] = tmp
                    heappush(hq, (AOJ[nr][nc], nr, nc))


N, M = map(int, input().split())
miro = tuple(tuple(map(int, list(input().rstrip()))) for _ in range(M))
print(dijkstra(0, 0))
