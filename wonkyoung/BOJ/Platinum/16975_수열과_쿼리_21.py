# 240604
# 43104 KB / 1144 ms
from sys import stdin

new_input = stdin.readline
N = int(new_input())
arr = [0] + list(map(int, new_input().split()))
M = int(new_input())
add_num = [0] * (4*N)

# 더할 값 찾기
def find_add_val(start, end, index, target):
    if start == target == end:
        return add_num[index]

    mid = (start + end) // 2
    if target <= mid:
        total = find_add_val(start, mid, index*2, target)
    else:
        total = find_add_val(mid+1, end, index*2+1, target)

    return total + add_num[index]

# 더할 값 표시
def add_k(start, end, index, left, right, k):
    if start > right or end < left:
        return
    if start >= left and end <= right:
        add_num[index] += k
        return

    mid = (start + end) // 2
    add_k(start, mid, index*2, left, right, k)
    add_k(mid+1, end, index*2+1, left, right, k)
    return


for _ in range(M):
    query = tuple(map(int, new_input().split()))
    if query[0] == 2:
        index = query[1]
        print(arr[index] + find_add_val(1, N, 1, index))
    else:
        add_k(1, N, 1, *query[1:])
