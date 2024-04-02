# 240402
# 33164 KB / 68 ms
from sys import stdin, setrecursionlimit

setrecursionlimit(10000)
new_input = stdin.readline
N = int(new_input())
max_level = max_width = 0
children = [() for _ in range(N+1)]
level_list = [0] * (N+1)
col_list = [-1] * (N+1)
col = 0

def plus_level(num):
    if children[num]:
        left, right = children[num]
        new_level = level_list[num] + 1
        if left != -1 and level_list[left] != new_level:
            level_list[left] = new_level
            plus_level(left)

        if right != -1 and level_list[right] != new_level:
            level_list[right] = level_list[num] + 1
            plus_level(right)

def in_order(node):
    global col
    if children[node]:
        left, right = children[node]
        if left != -1:
            in_order(left)
            if col_list[left] == -1:
                col_list[left] = col
                col += 1

        col_list[node] = col
        col += 1

        if right != -1:
            in_order(right)
            if col_list[right] == -1:
                col_list[right] = col
                col += 1

for _ in range(N):
    num, left, right = map(int, new_input().split())
    children[num] = (left, right)
    plus_level(num)

for i in range(1, N+1):
    if level_list[i] == 0:
        in_order(i)
        break

same_level_col = [[] for _ in range(N+1)]

for i in range(1, N+1):
    same_level_col[level_list[i]].append(col_list[i])

for i in range(N+1):
    if same_level_col[i]:
        min_val, max_val = min(same_level_col[i]), max(same_level_col[i])
        width = max_val - min_val + 1
        if width > max_width:
            max_width, max_level = width, i+1

    else:
        break

print(max_level, max_width)


# 32140 KB / 64 ms
from sys import stdin, setrecursionlimit

setrecursionlimit(10000) # 최대 깊이만큼 설정
new_input = stdin.readline
N = int(new_input())
max_level = max_width = 0
children = [() for _ in range(N+1)] # 각 노드별 자식
level_list = [0] * (N+1) # 각 노드별 레벨
col_list = [-1] * (N+1) # 각 노드별 열
col = 0 # 열 번호

# level 갱신
def plus_level(num):
    if children[num]:
        left, right = children[num]
        new_level = level_list[num] + 1
        if left != -1 and level_list[left] != new_level:
            level_list[left] = new_level
            plus_level(left)

        if right != -1 and level_list[right] != new_level:
            level_list[right] = level_list[num] + 1
            plus_level(right)

# 열 번호 갱신
def in_order(node):
    global col
    if children[node]:
        left, right = children[node]
        if left != -1:
            in_order(left)
            if col_list[left] == -1:
                col_list[left] = col
                col += 1

        col_list[node] = col
        col += 1

        if right != -1:
            in_order(right)
            if col_list[right] == -1:
                col_list[right] = col
                col += 1

# 입력받으면서 노드별 자식, 레벨 갱신
for _ in range(N):
    num, left, right = map(int, new_input().split())
    children[num] = (left, right)
    plus_level(num)

# 루트 찾아 중위 순회를 통해 열 번호 찾기
for i in range(1, N+1):
    if level_list[i] == 0:
        in_order(i)
        break

# 레벨별 열 번호 목록
same_level_col = [[] for _ in range(max(level_list)+1)]

for i in range(1, N+1):
    same_level_col[level_list[i]].append(col_list[i])

# 레벨별 너비 구해 최대 너비와 그때의 레벨 찾기
for i in range(len(same_level_col)):
    min_val, max_val = min(same_level_col[i]), max(same_level_col[i])
    width = max_val - min_val + 1
    if width > max_width:
        max_width, max_level = width, i+1

print(max_level, max_width)