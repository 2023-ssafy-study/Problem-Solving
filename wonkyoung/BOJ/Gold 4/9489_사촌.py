#231103
# 231106
# 31120 KB / 1468 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

while True:
    n, k = to_int()
    if n == 0:
        break
    node_list = list(to_int()) # 각 노드 정보
    if node_list[0] == k:
        print(0)
    else:
        node_info = {node_list[0] : (0, 0)} # 노드 번호 : (레벨, 부모)
        parent_idx = -1
        for i in range(1, n):
            node = node_list[i]
            if node_list[i-1] + 1 != node:
                parent_idx += 1
            parent_num = node_list[parent_idx]
            node_info[node] = (node_info[parent_num][0]+1 , parent_num)

        target_level, target_parent = node_info[k]
        if target_level == 1:
            print(0)
        else:
            target_grand_parent = node_info[target_parent][1]
            cnt = 0
            for i in node_list:
                level, parent = node_info[i]
                if level == target_level:
                    if parent != target_parent and node_info[parent][1] == target_grand_parent:
                        cnt += 1
                elif level > target_level:
                    break
            print(cnt)



# 31252 KB / 956 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

def return_cousin():
    n, k = to_int()
    if n == 0:
        return -1

    node_list = list(to_int()) # 각 노드 정보
    if node_list[0] == k:
        return 0

    node_info = {node_list[0] : (0, 0)} # 노드 번호 : (레벨, 부모)
    parent_idx = -1
    for i in range(1, n):
        node = node_list[i]
        if node_list[i-1] + 1 != node:
            parent_idx += 1
        parent_num = node_list[parent_idx]
        node_info[node] = (node_info[parent_num][0]+1 , parent_num)

    target_level, target_parent = node_info[k]

    if target_level == 1:
        return 0

    target_grand_parent = node_info[target_parent][1]
    cnt = 0
    for i in node_list:
        level, parent = node_info[i]
        if level == target_level:
            if parent != target_parent and node_info[parent][1] == target_grand_parent:
                cnt += 1
        elif level > target_level:
            return cnt
    return cnt

while True:
    answer = return_cousin()
    if answer == -1:
        break
    print(answer)


# 31120 KB / 968 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

def return_cousin():
    n, k = to_int()
    if n == 0:
        return -1

    node_list = list(to_int()) # 각 노드 정보
    if node_list[0] == k:
        return 0

    node_info = {node_list[0]: (0, 0)} # 노드 번호 : (레벨, 부모)
    parent_idx = -1
    for i in range(1, n):
        node = node_list[i]
        if node_list[i-1] + 1 != node:
            parent_idx += 1
        parent_num = node_list[parent_idx]
        node_info[node] = (node_info[parent_num][0] + 1, parent_num)

    target_level, target_parent = node_info[k]

    if target_level == 1:
        return 0

    target_grand_parent = node_info[target_parent][1]
    cnt = 0
    for i in node_list:
        level, parent = node_info[i]
        if level == target_level:
            if parent != target_parent and node_info[parent][1] == target_grand_parent:
                cnt += 1
        elif level > target_level:
            return cnt
    return cnt

while True:
    answer = return_cousin()
    if answer == -1:
        break
    print(answer)


# 31120 KB / 936 ms
from sys import stdin

def to_int():
    return map(int, stdin.readline().split())

def return_cousin():
    n, k = to_int()
    if n == 0:
        return -1

    node_list = list(to_int()) # 각 노드 정보
    node_info = {node_list[0]: (0, 0)} # 노드 번호 : (레벨, 부모)
    parent_idx = -1

    for i in range(1, n):
        node = node_list[i]
        if node_list[i-1] + 1 != node:
            parent_idx += 1
        parent_num = node_list[parent_idx]
        node_info[node] = (node_info[parent_num][0] + 1, parent_num)

    target_level, target_parent = node_info[k]

    if target_level <= 1:
        return 0

    target_grand_parent = node_info[target_parent][1]
    cnt = 0
    for i in node_list:
        level, parent = node_info[i]
        if level == target_level:
            if parent != target_parent and node_info[parent][1] == target_grand_parent:
                cnt += 1
        elif level > target_level:
            return cnt
    return cnt

while True:
    answer = return_cousin()
    if answer == -1:촌
        break
    print(answer)
