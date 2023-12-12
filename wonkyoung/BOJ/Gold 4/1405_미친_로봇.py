#230807
# 31256 KB / 1984 ms
def calc_probability():
    N, *probability = list(map(int, input().split()))

    def div_100(num):
        return num/100

    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    simple = 0
    probability = list(map(div_100, probability))
    visited = [[False] * (2*N+1) for _ in range(2*N+1)]
    visited[N][N] = True

    def add_cases(level=0, y=N, x=N, each=1):
        nonlocal simple
        if level == N:
            simple += each
            return

        for i in range(4):
            if probability[i] != 0:
                ny, nx = y+direct[i][0], x+direct[i][1]
                if 0 <= ny < 2*N+1 and 0 <= nx < 2*N+1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    add_cases(level+1, ny, nx, each*probability[i])
                    visited[ny][nx] = False

    add_cases()

    return simple

print(calc_probability())