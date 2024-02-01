# 240201
# 33660 KB / 220 ms
from sys import stdin
new_input = stdin.readline
N, K = map(int, new_input().split())
students = [len(new_input().rstrip()) for _ in range(N)]
total_cnt = 0
cnt_list = [0] * 21

for i in range(K):
    cnt_list[students[i]] += 1

end = K
for start in range(N-K):
    cnt_list[students[end]] += 1
    total_cnt += (cnt_list[students[start]] - 1)
    cnt_list[students[start]] -= 1
    end += 1

for start in range(N-K, N):
    total_cnt += (cnt_list[students[start]] - 1)
    cnt_list[students[start]] -= 1

print(total_cnt)



# 33660 KB / 216 ms
from sys import stdin
new_input = stdin.readline
N, K = map(int, new_input().split())
students = [len(new_input().rstrip()) for _ in range(N)]
total_cnt = 0
cnt_list = [0] * 21

for i in range(K):
    cnt_list[students[i]] += 1

end = K
for start in range(N-K):
    cnt_list[students[end]] += 1
    cnt_list[students[start]] -= 1
    total_cnt += cnt_list[students[start]]
    end += 1

for start in range(N-K, N):
    cnt_list[students[start]] -= 1
    total_cnt += cnt_list[students[start]]

print(total_cnt)


# 33660 KB / 228 ms
from sys import stdin
new_input = stdin.readline
N, K = map(int, new_input().split())
students = [len(new_input().rstrip()) for _ in range(N)]
total_cnt = 0
cnt_list = [0] * 21

for i in range(K):
    cnt_list[students[i]] += 1

end = K
for start in range(N-K):
    end_val, start_val = students[end], students[start]
    if end_val != start_val:
        cnt_list[end_val] += 1
        cnt_list[start_val] -= 1
    total_cnt += cnt_list[start_val]
    end += 1

for start in range(N-K, N):
    start_val = students[start]
    cnt_list[start_val] -= 1
    total_cnt += cnt_list[start_val]

print(total_cnt)



# 33660 KB / 168 ms
def calc_total_cnt():
    total_cnt = 0
    cnt_list = [0] * 21

    for i in range(K):
        cnt_list[students[i]] += 1

    end = K
    for start in range(N-K):
        cnt_list[students[end]] += 1
        cnt_list[students[start]] -= 1
        total_cnt += cnt_list[students[start]]
        end += 1

    for start in range(N-K, N):
        cnt_list[students[start]] -= 1
        total_cnt += cnt_list[students[start]]

    return total_cnt


from sys import stdin
new_input = stdin.readline
N, K = map(int, new_input().split())
students = [len(new_input().rstrip()) for _ in range(N)]

print(calc_total_cnt())