A = {}
A[0] = 1
N, P, Q = map(int, input().split())
def dp(n):
    global A
    if n not in A:
        A[n] = dp(n//P) + dp(n//Q)
    return A[n]
dp(N)
print(A[N])
