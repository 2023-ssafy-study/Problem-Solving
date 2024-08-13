# 240813
# 73040 KB / 6968 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    while True:
        N, M = int_input()
        if N == 0:
            return

        matrix = [list(int_input()) for _ in range(N)]
        check = [[0] * (M+1) for _ in range(N+1)]
        max_size = 0

        for i in range(1, N+1):
            for j in range(1, M+1):
                if matrix[i-1][j-1]:
                    size = min(check[i-1][j], check[i][j-1], check[i-1][j-1]) + 1
                    check[i][j] = size
                    if size > max_size:
                        max_size = size

        print(max_size)


main()



# 65128 KB / 6748 ms
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
