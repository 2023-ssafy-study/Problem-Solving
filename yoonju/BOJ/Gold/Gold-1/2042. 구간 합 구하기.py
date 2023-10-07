# 163,848 KB 880 ms

import sys

def init_tree(start, end, index):
    # start == end => 리프 노드
    if start == end:
        tree[index] = arr[start-1]
        return tree[index]
    mid = (start + end) // 2
    # 현재 노드 = 왼쪽 아래 노드 + 오른쪽 아래 노드
    tree[index] = init_tree(start, mid, index*2) + init_tree(mid+1, end, index*2+1)
    return tree[index]

def find_node(start, end, index, left, right):
    # 범위 벗어나면 0
    if start > right or end < left:
        return 0
    # 범위 내에 있으면 tree[index]
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    res = find_node(start, mid, index*2, left, right) + find_node(mid+1, end, index*2+1, left, right)
    return res

def change_value(start, end, index, change_index, value):
    # 범위 벗어나면 return
    if start > change_index or end < change_index:
        return

    tree[index] += value

    if start == end:
        return

    mid = (start + end) // 2
    change_value(start, mid, index*2, change_index, value)
    change_value(mid+1, end, index*2+1, change_index, value)

N, M, K = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]

tree = [0]*(N*4)

init_tree(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        change_value(1, N, 1, b, c-arr[b-1])
        arr[b-1] = c
    elif a == 2:
        answer = find_node(1, N, 1, b, c)
        print(answer)