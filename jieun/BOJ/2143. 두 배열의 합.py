T = int(input())
n = int(input())
A = tuple(map(int, input().split()))
m = int(input())
B = tuple(map(int, input().split()))

# 누적합
a_ps, b_ps = [0] * (n + 1), [0] * (m + 1)
for i in range(1, n + 1):
    a_ps[i] = a_ps[i - 1] + A[i - 1]
for j in range(1, m + 1):
    b_ps[j] = b_ps[j - 1] + B[j - 1]

# 부 배열의 합
a_subs, b_subs = {}, {}
for i in range(1, n + 1):
    for j in range(i, n + 1):
        a_subs[a_ps[j] - a_ps[i - 1]] = a_subs.get(a_ps[j] - a_ps[i - 1], 0) + 1
for i in range(1, m + 1):
    for j in range(i, m + 1):
        b_subs[b_ps[j] - b_ps[i - 1]] = b_subs.get(b_ps[j] - b_ps[i - 1], 0) + 1

answer = 0
for ak in a_subs:
    if T-ak in b_subs:
        answer += a_subs[ak]*b_subs[T-ak]
print(answer)