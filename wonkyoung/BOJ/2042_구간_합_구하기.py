# 230918
from sys import stdin
N, M, K = map(int, stdin.readline().split())
numbers = [0] * (4*N)
initial_numbers = [int(stdin.readline()) for _ in range(N)]

def fill_numbers(left_limit=0, right_limit=N-1, index=1):
    if left_limit == right_limit:
        numbers[index] = initial_numbers[right_limit]
    else:
        mid = (left_limit + right_limit)//2
        numbers[index] = fill_numbers(left_limit, mid, index*2) + fill_numbers(mid+1, right_limit, index*2+1)
    return numbers[index]


def change_number(target_i, dif, left_limit=0, right_limit=N-1, index=1):
    if target_i < left_limit or target_i > right_limit:
        return
    numbers[index] += dif
    if left_limit == right_limit:
        return
    mid = (left_limit + right_limit) // 2
    change_number(target_i, dif, left_limit, mid, index*2)
    change_number(target_i, dif, mid+1, right_limit, index*2+1)

def find_sum(start, end, left_limit=0, right_limit=N-1, index=1):
    if start > right_limit or end < left_limit:
        return 0
    if start <= left_limit and end >= right_limit:
        return numbers[index]
    mid = (left_limit + right_limit) // 2
    return find_sum(start, end, left_limit, mid, index*2) + find_sum(start, end, mid+1, right_limit, index*2+1)

fill_numbers()

for _ in range(M+K):
    a, b, c = map(int, stdin.readline().split())
    b -= 1
    if a == 1:
        change_number(b, c - initial_numbers[b])
        initial_numbers[b] = c
    else:
        c -= 1
        print(find_sum(b, c))



#
from sys import stdin
N, M, K = map(int, stdin.readline().split())
numbers = [0] * (4*N)
initial_numbers = [0] + [int(stdin.readline()) for _ in range(N)]

def fill_numbers(left_limit=1, right_limit=N, index=1):
    if left_limit == right_limit:
        numbers[index] = initial_numbers[right_limit]
    else:
        mid = (left_limit + right_limit)//2
        numbers[index] = fill_numbers(left_limit, mid, index*2) + fill_numbers(mid+1, right_limit, index*2+1)
    return numbers[index]


def change_number(target_i, dif, left_limit=1, right_limit=N, index=1):
    if target_i < left_limit or target_i > right_limit:
        return
    numbers[index] += dif
    if left_limit == right_limit:
        return
    mid = (left_limit + right_limit) // 2
    change_number(target_i, dif, left_limit, mid, index*2)
    change_number(target_i, dif, mid+1, right_limit, index*2+1)

def find_sum(start, end, left_limit=1, right_limit=N, index=1):
    if start > right_limit or end < left_limit:
        return 0
    if start <= left_limit and end >= right_limit:
        return numbers[index]
    mid = (left_limit + right_limit) // 2
    return find_sum(start, end, left_limit, mid, index*2) + find_sum(start, end, mid+1, right_limit, index*2+1)

fill_numbers()

for _ in range(M+K):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        change_number(b, c - initial_numbers[b])
        initial_numbers[b] = c
    else:
        print(find_sum(b, c))


#
def fill_numbers(left_limit, right_limit, index):
    if left_limit == right_limit:
        numbers[index] = initial_numbers[right_limit]
    else:
        mid = (left_limit + right_limit)//2
        numbers[index] = fill_numbers(left_limit, mid, index*2) + fill_numbers(mid+1, right_limit, index*2+1)
    return numbers[index]


def change_number(target_i, dif, left_limit, right_limit, index):
    if target_i < left_limit or target_i > right_limit:
        return
    numbers[index] += dif
    if left_limit == right_limit:
        return
    mid = (left_limit + right_limit) // 2
    change_number(target_i, dif, left_limit, mid, index*2)
    change_number(target_i, dif, mid+1, right_limit, index*2+1)

def find_sum(start, end, left_limit, right_limit, index):
    if start > right_limit or end < left_limit:
        return 0
    if start <= left_limit and end >= right_limit:
        return numbers[index]
    mid = (left_limit + right_limit) // 2
    return find_sum(start, end, left_limit, mid, index*2) + find_sum(start, end, mid+1, right_limit, index*2+1)


from sys import stdin
N, M, K = map(int, stdin.readline().split())
numbers = [0] * (4*N)
initial_numbers = [0]
for _ in range(N):
    initial_numbers.append(int(stdin.readline()))

fill_numbers(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        change_number(b, c - initial_numbers[b], 1, N, 1)
        initial_numbers[b] = c
    else:
        print(find_sum(b, c, 1, N, 1))