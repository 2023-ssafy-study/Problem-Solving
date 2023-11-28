# 231124
# 346424 KB / 3280 ms (Python 3) 287676 KB / 1032 ms (Pypy 3)
from sys import stdin
N = int(stdin.readline())
schedule = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = [0] * (N+1)
max_val = 0
for i in range(N):
    day, pay = schedule[i]
    new_day = i+day
    if result[i] < max_val:
        result[i] = max_val
    if new_day <= N:
        new_pay = pay+result[i]
        if new_pay > result[new_day]:
            result[new_day] = new_pay
    if max_val < result[i]:
        max_val = result[i]

print(max(result))


# 3204 KB / 347448 KB (Python 3)
from sys import stdin
N = int(stdin.readline())
schedule = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = [0] * (N+1)
max_val = 0
for i in range(N):
    day, pay = schedule[i]
    new_day = i+day
    if result[i] < max_val:
        result[i] = max_val
    if new_day <= N:
        new_pay = pay+result[i]
        if new_pay > result[new_day]:
            result[new_day] = new_pay
    if max_val < result[i]:
        max_val = result[i]

print(max(max_val, result[-1]))



# 97108 KB / 1964 ms (Python 3) 122416 KB / 508 ms (Pypy 3)
from sys import stdin
N = int(stdin.readline())
result = [0] * (N+1)
max_val = 0
for i in range(N):
    day, pay = map(int, stdin.readline().split())
    new_day = i+day
    if result[i] < max_val:
        result[i] = max_val
    if new_day <= N:
        new_pay = pay+result[i]
        if new_pay > result[new_day]:
            result[new_day] = new_pay
    if max_val < result[i]:
        max_val = result[i]

print(max(max_val, result[-1]))



# 97108 KB / 1936 ms (Python 3) 122416 KB / 516 ms (Pypy 3)
from sys import stdin
N = int(stdin.readline())
result = [0] * (N+1)
max_val = 0
for i in range(N):
    day, pay = map(int, stdin.readline().split())
    new_day = i+day
    if result[i] < max_val:
        result[i] = max_val
    else:
        max_val = result[i]

    if new_day <= N:
        new_pay = pay+result[i]
        if new_pay > result[new_day]:
            result[new_day] = new_pay

print(max(max_val, result[-1]))


# 97108 KB / 1196 ms (Python 3) 122676 KB / 532 ms (Pypy 3)
def find_max_revenue():
    from sys import stdin
    N = int(stdin.readline())
    result = [0] * (N+1)
    max_val = 0
    for i in range(N):
        day, pay = map(int, stdin.readline().split())
        new_day = i+day
        if result[i] < max_val:
            result[i] = max_val
        else:
            max_val = result[i]

        if new_day <= N:
            new_pay = pay+result[i]
            if new_pay > result[new_day]:
                result[new_day] = new_pay

    return max(max_val, result[-1])

print(find_max_revenue())