# 231106
# 43684 KB / 4480 ms
from sys import stdin
N = int(stdin.readline())
if N == 1:
    print(0)
else:
    children = [[] for _ in range(N+1)]
    for _ in range(N):
        a, b, c = map(int, input().split())
        children[a] = [b, c]

    cnt_list = [2] * (N+1)
    if children[1][1] != -1:
        right_root = children[1][1]
        cnt_list[right_root] = 1

        while True:
            left_child, right_child = children[right_root]
            if right_child != -1:
                cnt_list[right_child] = 1
                right_root = right_child
            else:
                break

    print(sum(cnt_list[2:]))


# 34592 KB / 3996 ms
def cnt_visited():
    from sys import stdin
    N = int(stdin.readline())
    if N == 1:
        return 0

    right_child = [0] * (N+1)
    for _ in range(N):
        a, b, c = map(int, input().split())
        right_child[a] = c

    cnt_list = [2] * (N + 1)

    if right_child[1] != -1:
        right_root = right_child[1]
        cnt_list[right_root] = 1

        while True:
            if right_child[right_root] != -1:
                right_root = right_child[right_root]
                cnt_list[right_root] = 1
            else:
                return sum(cnt_list[2:])

    return sum(cnt_list[2:])

print(cnt_visited())


# 34592 KB / 3948 ms
def cnt_visited():
    from sys import stdin
    N = int(stdin.readline())
    if N == 1:
        return 0

    right_child = [0] * (N + 1)
    for _ in range(N):
        a, b, c = map(int, input().split())
        right_child[a] = c

    cnt_list = [2] * (N + 1)
    right_root = 1

    while True:
        if right_child[right_root] != -1:
            right_root = right_child[right_root]
            cnt_list[right_root] = 1
        else:
            return sum(cnt_list[2:])

print(cnt_visited())


# 34592 KB / 124 ms
def cnt_visited():
    from sys import stdin
    N = int(stdin.readline())
    if N == 1:
        return 0

    right_child = [0] * (N + 1)
    for _ in range(N):
        a, b, c = map(int, stdin.readline().split())
        right_child[a] = c

    cnt_list = [2] * (N + 1)
    right_root = 1

    while True:
        if right_child[right_root] != -1:
            right_root = right_child[right_root]
            cnt_list[right_root] = 1
        else:
            return sum(cnt_list[2:])

print(cnt_visited())

