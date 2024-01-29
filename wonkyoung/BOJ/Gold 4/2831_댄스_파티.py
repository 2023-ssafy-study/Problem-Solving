# 240129
# 46952 KB / 164 ms
'''
2
-1800 -2200
1900 1700

2
1900 1700
-1800 -2200
'''
N = int(input())
height_m = [[] for _ in range(2)] # +, -
height_w = [[] for _ in range(2)] # -, +
for height in map(int, input().split()):
    if height > 0:
        height_m[0].append(height)
    else:
        height_m[1].append(-height)

for height in map(int, input().split()):
    if height < 0:
        height_w[0].append(-height)
    else:
        height_w[1].append(height)

for i in range(2):
    height_m[i].sort()
    height_w[i].sort()

cnt = 0

w_i = len(height_w[0])-1
if w_i >= 0:
    for i in range(len(height_m[0])-1, -1, -1):
        ref = height_m[0][i]
        if height_w[0][w_i] > ref:
            cnt += 1
            w_i -= 1
            if w_i < 0:
                break

w_i, w_limit = 0, len(height_w[1])
if w_limit >= 1:
    for ref in height_m[1]:
        if height_w[1][w_i] < ref:
            cnt += 1
            w_i += 1
            if w_i >= w_limit:
                break

print(cnt)