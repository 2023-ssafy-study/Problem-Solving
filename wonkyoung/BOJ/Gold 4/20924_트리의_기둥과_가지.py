# 230401
# 144676 KB / 1248 ms
from sys import stdin
from collections import deque

def to_int():
    return map(int, stdin.readline().split())

N, R = to_int()
link_info = [[] for _ in range(N+1)]
children = [[] for _ in range(N+1)]
visited = [False] * (N+1)
tree_info = []
q = deque()
for _ in range(N-1):
    a, b, d = to_int()
    link_info[a].append((b, d))
    link_info[b].append((a, d))

# 부모 자식 관계 파악하기
q.append(R)
visited[R] = True
while q:
    node = q.popleft()
    for child, distance in link_info[node]:
        if not visited[child]:
            visited[child] = True
            q.append(child)
            children[node].append((child, distance))

# 기가 노드와 기둥의 길이 찾기
node, length = R, 0
while True:
    if len(children[node]) != 1:
        break
    length += children[node][0][1]
    node = children[node][0][0]

tree_info.append(length)

# 가장 긴 가지 길이 찾기
length = 0
q.append((node, 0))
while q:
    node, total = q.popleft()
    if not children[node]:
        if total > length:
            length = total
    else:
        for new_node, distance in children[node]:
            q.append((new_node, total+distance))

tree_info.append(length)

print(*tree_info)



# 시간 초과
from sys import stdin, setrecursionlimit

def to_int():
    return map(int, stdin.readline().split())

N, R = to_int()
if N > 1000:
    setrecursionlimit(N)
link_info = [[] for _ in range(N+1)]
visited = [False] * (N+1)
giga_node = length = 0
tree_info = []
for _ in range(N-1):
    a, b, d = to_int()
    link_info[a].append((b, d))
    link_info[b].append((a, d))

def dfs(node, total):
    global giga_node, length
    next_node_list = []
    # 부모 자식 관계 파악하기
    for child, distance in link_info[node]:
        if not visited[child]:
            visited[child] = True
            next_node_list.append((child, distance))

    if len(next_node_list) == 0:
        # 가장 긴 가지 길이 찾기
        if total > length:
            length = total

    # 기가 노드와 기둥의 길이 찾기
    if giga_node == 0 and len(next_node_list) != 1:
        giga_node = node
        tree_info.append(total)

    for child, distance in next_node_list:
        dfs(child, total+distance)


visited[R] = True
dfs(R, 0)
tree_info.append(length - tree_info[0])
print(*tree_info)