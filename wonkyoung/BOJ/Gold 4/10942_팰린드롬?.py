# 240213
# 46300 KB / 2072 ms
from sys import stdin
new_input = stdin.readline

N = int(new_input())
numbers = [''] + new_input().split()
check = [[-1] * (i+1) for i in range(N+1)]

for mid in range(1, N+1):
    check[mid][mid] = 1
    for start, end in (mid - 1, mid + 1), (mid, mid + 1):
        flag = 1
        while start >= 1 and end <= N:
            if numbers[start] != numbers[end]:
                flag = 0
            check[end][start] = flag
            start -= 1
            end += 1

M = int(new_input())
for _ in range(M):
    S, E = map(int, new_input().split())
    print(check[E][S])



# 61932 KB / 2052 ms
from sys import stdin
new_input = stdin.readline

N = int(new_input())
numbers = [''] + new_input().split()
check = [[-1] * (N+1) for _ in range(N+1)]

for mid in range(1, N+1):
    check[mid][mid] = 1
    for start, end in (mid - 1, mid + 1), (mid, mid + 1):
        flag = 1
        while start >= 1 and end <= N:
            if numbers[start] != numbers[end]:
                flag = 0
            check[end][start] = flag
            start -= 1
            end += 1

M = int(new_input())
for _ in range(M):
    S, E = map(int, new_input().split())
    print(check[E][S])


# 46300 KB / 2068 ms
from sys import stdin
new_input = stdin.readline

N = int(new_input())
numbers = [''] + new_input().split()
check = [[0] * (i+1) for i in range(N+1)]

for mid in range(1, N+1):
    check[mid][mid] = 1
    for start, end in (mid - 1, mid + 1), (mid, mid + 1):
        while start >= 1 and end <= N:
            if numbers[start] != numbers[end]:
                break
            check[end][start] = 1
            start -= 1
            end += 1

M = int(new_input())
for _ in range(M):
    S, E = map(int, new_input().split())
    print(check[E][S])
