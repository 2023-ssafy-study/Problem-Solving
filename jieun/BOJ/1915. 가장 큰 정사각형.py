n, m = map(int, input().split())
max_len = 0
sq = [list(map(int, list(input()))) for _ in range(n)]

for r in range(n):
    for c in range(m):
        if sq[r][c] == 1 and r > 0 and c > 0:
            sq[r][c] += min(sq[r - 1][c - 1], sq[r - 1][c], sq[r][c - 1])
        max_len = max(max_len, sq[r][c])

print(max_len * max_len)
