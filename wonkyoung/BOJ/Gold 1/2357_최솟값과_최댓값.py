# 240603
# 41228 KB / 2340 ms
from sys import stdin
new_input = stdin.readline

N, M = map(int, new_input().split())
arr = [int(new_input()) for _ in range(N)]
limit = int(1e9)+1
max_val = [0] * (4*N)
min_val = [0] * (4*N)

def fill_list(start, end, index):
    if start == end:
        max_val[index] = min_val[index] = arr[start]
        return (min_val[index], max_val[index])

    mid = (start + end)//2
    min_left, max_left = fill_list(start, mid, index*2)
    min_right, max_right = fill_list(mid+1, end, index*2+1)
    min_val[index] = min(min_left, min_right)
    max_val[index] = max(max_left, max_right)
    return (min_val[index], max_val[index])

def find_val(start, end, index, left, right):
    if left > end or right < start:
        return (limit, 0)
    if left <= start and right >= end:
        return (min_val[index], max_val[index])

    mid = (start + end) // 2
    min_left, max_left = find_val(start, mid, index*2, left, right)
    min_right, max_right = find_val(mid+1, end, index*2+1, left, right)
    return (min(min_left, min_right), max(max_left, max_right))

fill_list(0, N-1, 1)

for _ in range(M):
    start, end = map(int, new_input().split())
    print(*find_val(0, N-1, 1, start-1, end-1))



# 41228 KB / 2340 ms
from sys import stdin
new_input = stdin.readline

N, M = map(int, new_input().split())
arr = [0] + [int(new_input()) for _ in range(N)]
limit = int(1e9)+1
max_val = [0] * (4*N)
min_val = [0] * (4*N)

def fill_list(start, end, index):
    if start == end:
        max_val[index] = min_val[index] = arr[start]
        return (min_val[index], max_val[index])

    mid = (start + end)//2
    min_left, max_left = fill_list(start, mid, index*2)
    min_right, max_right = fill_list(mid+1, end, index*2+1)
    min_val[index] = min(min_left, min_right)
    max_val[index] = max(max_left, max_right)
    return (min_val[index], max_val[index])

def find_val(start, end, index, left, right):
    if left > end or right < start:
        return (limit, 0)
    if left <= start and right >= end:
        return (min_val[index], max_val[index])

    mid = (start + end) // 2
    min_left, max_left = find_val(start, mid, index*2, left, right)
    min_right, max_right = find_val(mid+1, end, index*2+1, left, right)
    return (min(min_left, min_right), max(max_left, max_right))

fill_list(1, N, 1)

for _ in range(M):
    start, end = map(int, new_input().split())
    print(*find_val(1, N, 1, start, end))


# 51396 KB / 2372 ms
from sys import stdin
new_input = stdin.readline

N, M = map(int, new_input().split())
arr = [0] + [int(new_input()) for _ in range(N)]
limit = int(1e9)+1
min_max = [() for _ in range(4*N)]

def fill_list(start, end, index):
    if start == end:
        min_max[index] = (arr[start],)*2
        return min_max[index]

    mid = (start + end)//2
    min_left, max_left = fill_list(start, mid, index*2)
    min_right, max_right = fill_list(mid+1, end, index*2+1)
    min_max[index] = (min(min_left, min_right), max(max_left, max_right))
    return min_max[index]

def find_val(start, end, index, left, right):
    if left > end or right < start:
        return (limit, 0)
    if left <= start and right >= end:
        return min_max[index]

    mid = (start + end) // 2
    min_left, max_left = find_val(start, mid, index*2, left, right)
    min_right, max_right = find_val(mid+1, end, index*2+1, left, right)
    return (min(min_left, min_right), max(max_left, max_right))

fill_list(1, N, 1)

for _ in range(M):
    start, end = map(int, new_input().split())
    print(*find_val(1, N, 1, start, end))


# 41228 KB / 2460 ms
from sys import stdin
new_input = stdin.readline

N, M = map(int, new_input().split())
arr = [0] + [int(new_input()) for _ in range(N)]
limit = int(1e9)+1
max_val = [0] * (4*N)
min_val = [0] * (4*N)

def return_min_max(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))

def fill_list(start, end, index):
    if start == end:
        max_val[index] = min_val[index] = arr[start]
        return (min_val[index], max_val[index])

    mid = (start + end)//2
    left = fill_list(start, mid, index*2)
    right = fill_list(mid+1, end, index*2+1)
    min_val[index], max_val[index] = return_min_max(left, right)
    return (min_val[index], max_val[index])

def find_val(start, end, index, left, right):
    if left > end or right < start:
        return (limit, 0)
    if left <= start and right >= end:
        return (min_val[index], max_val[index])

    mid = (start + end) // 2
    left_val = find_val(start, mid, index*2, left, right)
    right_val = find_val(mid+1, end, index*2+1, left, right)
    return return_min_max(left_val, right_val)

fill_list(1, N, 1)

for _ in range(M):
    start, end = map(int, new_input().split())
    print(*find_val(1, N, 1, start, end))
