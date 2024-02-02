# 240202
# 47380 KB / 596 ms
from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    N, M, K = map(int, new_input().split())
    finance = list(map(int, new_input().split()))
    if M < N:
        finance += finance[:M-1]
        stolen = cnt = 0
        for i in range(M-1):
            stolen += finance[i]

        end = M-1
        for start in range(N):
            stolen += finance[end]
            if stolen < K:
                cnt += 1
            stolen -= finance[start]
            end += 1

        print(cnt)
    else:
        print(1 if sum(finance) < K else 0)



# 47380 KB / 612 ms
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    finance = list(map(int, input().split()))
    if M != N:
        finance += finance[:M-1]
        stolen = cnt = 0
        for i in range(M-1):
            stolen += finance[i]

        end = M-1
        for start in range(N):
            stolen += finance[end]
            if stolen < K:
                cnt += 1
            stolen -= finance[start]
            end += 1

        print(cnt)
    else:
        print(1 if sum(finance) < K else 0)


# 47380 KB / 632 ms
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    finance = list(map(int, input().split()))
    if M < N:
        finance += finance[:M-1]
        stolen = cnt = 0
        for i in range(M-1):
            stolen += finance[i]

        end = M-1
        for start in range(N):
            stolen += finance[end]
            if stolen < K:
                cnt += 1
            stolen -= finance[start]
            end += 1

        print(cnt)
    else:
        print(1 if sum(finance) < K else 0)


# 47036 KB / 640 ms
from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    N, M, K = map(int, new_input().split())
    finance = list(map(int, new_input().split()))
    if M < N:
        stolen = cnt = 0
        for i in range(M-1):
            stolen += finance[i]

        end = M-1
        for start in range(N):
            stolen += finance[end%N]
            if stolen < K:
                cnt += 1
            stolen -= finance[start]
            end += 1

        print(cnt)
    else:
        print(1 if sum(finance) < K else 0)



# 47380 KB / 380 ms
def cnt_cases(N, M, K, finance):
    if N == M:
        return 1 if sum(finance) < K else 0

    finance += finance[:M-1]
    stolen = cnt = 0
    for i in range(M-1):
        stolen += finance[i]

    end = M-1
    for start in range(N):
        stolen += finance[end]
        if stolen < K:
            cnt += 1
        stolen -= finance[start]
        end += 1

    return cnt

from sys import stdin
new_input = stdin.readline
T = int(new_input())
for _ in range(T):
    N, M, K = map(int, new_input().split())
    finance = list(map(int, new_input().split()))
    print(cnt_cases(N, M, K, finance))