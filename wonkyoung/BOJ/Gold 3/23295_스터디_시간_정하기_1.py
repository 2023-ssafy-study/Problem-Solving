# 240206
# 34972 MB / 388 ms
from sys import stdin
new_input = stdin.readline
N, T = map(int, new_input().split())
limit = int(1e5) + 1
schedule = [0] * limit
max_end = 0
for _ in range(N):
    K = int(new_input())
    for _ in range(K):
        S, E = map(int, new_input().split())
        schedule[S] += 1
        schedule[E] -= 1

    if E > max_end:
        max_end = E

for i in range(1, max_end+1):
    schedule[i] += schedule[i-1]

total = max_total = 0

end = T-1
final_start = final_end = 0
for i in range(end):
    total += schedule[i]

for start in range(max_end - T + 1):
    total += schedule[end]
    if total > max_total:
        max_total = total
        final_start, final_end = start, end+1
    total -= schedule[start]
    end += 1

print(final_start, final_end)



# 34972 MB / 384 ms
from sys import stdin
new_input = stdin.readline
N, T = map(int, new_input().split())
limit = int(1e5) + 1
schedule = [0] * limit
max_end = 0
for _ in range(N):
    K = int(new_input())
    for _ in range(K):
        S, E = map(int, new_input().split())
        schedule[S] += 1
        schedule[E] -= 1

    if E > max_end:
        max_end = E

for i in range(1, max_end+1):
    schedule[i] += schedule[i-1]

total = max_total = 0

end = T-1
final_start = final_end = 0
for i in range(end):
    total += schedule[i]

for start in range(max_end - T + 1):
    total += schedule[end]
    end += 1
    if total > max_total:
        max_total = total
        final_start, final_end = start, end
    total -= schedule[start]

print(final_start, final_end)



# 34972 MB / 388 ms
from sys import stdin
new_input = stdin.readline
N, T = map(int, new_input().split())
schedule = [0] * (int(1e5) + 1)
max_end = 0
for _ in range(N):
    K = int(new_input())
    for _ in range(K):
        S, E = map(int, new_input().split())
        schedule[S] += 1
        schedule[E] -= 1

    if E > max_end:
        max_end = E

for i in range(1, max_end+1):
    schedule[i] += schedule[i-1]

total = max_total = 0

end = T-1
final_start = final_end = 0
for i in range(end):
    total += schedule[i]

for start in range(max_end - T + 1):
    total += schedule[end]
    end += 1
    if total > max_total:
        max_total = total
        final_start, final_end = start, end
    total -= schedule[start]

print(final_start, final_end)