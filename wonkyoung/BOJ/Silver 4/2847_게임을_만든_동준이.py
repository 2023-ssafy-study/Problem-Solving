# 231114
# 31120 KB / 44 ms
N = int(input())
score_list = [int(input()) for _ in range(N)]
cnt, limit = 0, score_list[-1]
for i in range(N-2, -1, -1):
    score = score_list[i]
    if score >= limit:
        cnt += score - limit + 1
        score = limit - 1
    limit = score

print(cnt)


# 31120 KB / 40 ms
N = int(input())
score_list = [int(input()) for _ in range(N)]
cnt, limit = 0, score_list[-1]
for i in range(N-2, -1, -1):
    score = score_list[i]
    if score >= limit:
        cnt += score - limit + 1
        limit -= 1
    else:
        limit = score

print(cnt)