# 240701
# 31708 KB / 204 ms
N, B, W = map(int, input().split())
info = input()
max_len = first_i = 0
cnt = {'B': 0, 'W': 0}
for i in range(N):
    cnt[info[i]] += 1
    if cnt['B'] > B:
        if cnt['W'] >= W:
            now_len = sum(cnt.values())-1
            if now_len > max_len:
                max_len = now_len
        while cnt['B'] > B:
            cnt[info[first_i]] -= 1
            first_i += 1

if cnt['W'] >= W:
    now_len = sum(cnt.values())
    if now_len > max_len:
        max_len = now_len

print(max_len)


# 31708 KB / 144 ms
N, B, W = map(int, input().split())
info = input()
max_len = first_i = b_cnt = w_cnt = 0
for i in range(N):
    alp = info[i]
    if alp == 'W':
        w_cnt += 1
    else:
        if b_cnt >= B:
            if w_cnt >= W:
                now_len = w_cnt + b_cnt
                if now_len > max_len:
                    max_len = now_len
            while True:
                if info[first_i] == 'W':
                    w_cnt -= 1
                    first_i += 1
                else:
                    b_cnt -= 1
                    first_i += 1
                    break
        b_cnt += 1

if w_cnt >= W:
    now_len = w_cnt + b_cnt
    if now_len > max_len:
        max_len = now_len

print(max_len)


# 31708 KB / 164 ms
N, B, W = map(int, input().split())
info = input()
max_len = first_i = b_cnt = w_cnt = 0

def change_max_len():
    global max_len

    if w_cnt >= W:
        now_len = w_cnt + b_cnt
        if now_len > max_len:
            max_len = now_len

def find_first_i():
    global first_i, w_cnt, b_cnt

    while True:
        if info[first_i] == 'W':
            w_cnt -= 1
            first_i += 1
        else:
            b_cnt -= 1
            first_i += 1
            break


for i in range(N):
    alp = info[i]
    if alp == 'W':
        w_cnt += 1
    else:
        if b_cnt >= B:
            change_max_len()
            find_first_i()
        b_cnt += 1

change_max_len()

print(max_len)
