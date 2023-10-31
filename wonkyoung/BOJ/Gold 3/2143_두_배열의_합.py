# 231031
def to_int():
    return int(input())
def to_int_list():
    return list(map(int, input().split()))

T = to_int()
N = to_int()
A = to_int_list()
M = to_int()
B = to_int_list()
cnt = 0
acc_a, acc_b = [A[0]], [B[0]]
for i in range(1, N):
    acc_a.append(acc_a[i-1] + A[i])
for i in range(1, M):
    acc_b.append(acc_b[i-1] + B[i])

num_cnt = {}

for i in range(M):
    for j in range(i, M):
        acc_num = acc_b[j] - acc_b[i-1] if i > 0 else acc_b[j]
        if num_cnt.get(acc_num):
            num_cnt[acc_num] += 1
        else:
            num_cnt[acc_num] = 1

for i in range(N):
    for j in range(i, N):
        target = T - (acc_a[j] - acc_a[i-1] if i > 0 else acc_a[j])
        cnt += num_cnt.get(target, 0)

print(cnt)
