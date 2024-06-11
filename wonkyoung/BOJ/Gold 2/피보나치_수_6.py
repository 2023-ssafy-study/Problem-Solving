#240611
# 31120 KB / 40 ms
def fibo(n):
    div_num = int(1e9)+7
    zero = [[1, 0], [0, 1]]
    base = [[1, 1], [1, 0]]

    def square_matrix_mul(a, b):
        new = [[0 for _ in range(2)] for _ in range(2)]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    new[i][j] = (new[i][j] + a[i][k] * b[k][j]) % div_num

        return new

    def get_nth(n):
        matrix = [zero[i][:] for i in range(2)]
        tmp = [base[i][:] for i in range(2)]
        k = 0

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)

        return matrix

    return get_nth(n)[1][0]


print(fibo(int(input())))
