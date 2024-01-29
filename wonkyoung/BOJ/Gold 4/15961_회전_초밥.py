# 240129
# 140952 KB / 2264 ms
from sys import stdin
new_input = stdin.readline
N, d, k, c = map(int, new_input().split())
chobap_rail = [int(new_input()) for _ in range(N)]
chobap_rail += chobap_rail[:k-1]
eaten = [0] * (d+1)
eaten[c] = 1
cnt = 1

for i in range(k-1):
    idx = chobap_rail[i]
    if eaten[idx] == 0:
        cnt += 1
    eaten[idx] += 1

max_cnt = cnt

for i in range(N):
    pre_idx, idx = chobap_rail[i], chobap_rail[i+k-1]
    if eaten[idx] == 0:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    eaten[idx] += 1
    eaten[pre_idx] -= 1
    if eaten[pre_idx] == 0:
        cnt -= 1

print(max_cnt)

# 140952 KB / 2400 ms
from sys import stdin
new_input = stdin.readline
N, d, k, c = map(int, new_input().split())
chobap_rail = [int(new_input()) for _ in range(N)]
chobap_rail += chobap_rail[:k-1]
eaten = [0] * (d+1)
eaten[c] = cnt = 1

for i in range(k-1):
    idx = chobap_rail[i]
    if eaten[idx] == 0:
        cnt += 1
    eaten[idx] += 1

max_cnt = cnt

for i in range(N):
    pre_idx, idx = chobap_rail[i], chobap_rail[i+k-1]
    if pre_idx != idx:
        if eaten[idx] == 0:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        eaten[idx] += 1
        eaten[pre_idx] -= 1
        if eaten[pre_idx] == 0:
            cnt -= 1

print(max_cnt)
