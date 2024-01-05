from heapq import heappush, heappop


def dijkstra():
    changed = [[float('inf')] * n for _ in range(n)]  # 흰 방으로 바꾸어야 할 최소의 검은 방의 수
    changed[0][0] = 0
    hq = []
    heappush(hq, (0, 0, 0))

    while hq:
        b, r, c = heappop(hq)
        if r == c == n - 1:
            print(b)
            return
        if changed[r][c] < b:   continue
        for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if 0 <= nr < n and 0 <= nc < n:
                tmp = b + 1 - rooms[nr][nc]  # 1-rooms[nr][nc]: 이번 방 바뀜 여부(흰 방이면 0, 검은 방이면 1)
                if tmp < changed[nr][nc]:
                    changed[nr][nc] = tmp
                    heappush(hq, (changed[nr][nc], nr, nc))


n = int(input())
rooms = tuple(tuple(map(int, list(input()))) for _ in range(n))
dijkstra()
