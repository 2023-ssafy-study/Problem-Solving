# 240813
# 34760 KB / 236 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    while True:
        N, M = int_input()
        if N == 0:
            return

        matrix = [list(int_input()) for _ in range(N)]
        max_size = 0

        for i in range(N):
            for j in range(M):
                if i > 0 and j > 0 and matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                
                if matrix[i][j] > max_size:
                    max_size = matrix[i][j]

        print(max_size)


main()



# 34088 KB / 236 ms
def can_clear():
    from collections import deque

    N, k = map(int, input().split())
    lines = [input() for _ in range(2)]
    visited = [[False] * N for _ in range(2)]

    q = deque()
    q.append((0, 0, 0))

    while q:
        r, c, time = q.popleft()
        if not visited[r][c]:
            nc1, nc2, nr, nc3 = c+1, c-1, 1-r, c+k
            visited[r][c] = True
            time += 1

            if nc1 >= N or nc2 >= N or nc3 >= N:
                return 1

            if lines[r][nc1] == '1':
                q.append((r, nc1, time))

            if nc2 >= time and lines[r][nc2] == '1':
                q.append((r, nc2, time))

            if lines[nr][nc3] == '1':
                q.append((nr, nc3, time))

    return 0

print(can_clear())
