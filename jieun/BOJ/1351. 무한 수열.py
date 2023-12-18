def cal(n):
    if n in A.keys():
        return A[n]
    A[n] = cal(n // P) + cal(n // Q)
    return A[n]


N, P, Q = map(int, input().split())
A = {0: 1}
print(cal(N))
