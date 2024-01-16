# 240115
from sys import stdin
from heapq import heappush, heappop
def to_int(): return map(int, stdin.readline().split())

N, T = to_int()
position = {} # {y : [x...], ...}
position_list = [] # [(x, y), ...]
heap = [(0, 0, 0)] # cnt, -y, x
visited = [N+1] * N
for i in range(N):
    x, y = to_int()
    position_list.append((x, y))
    if position.get(y):
        position[y].append((x, i))
    else:
        position[y] = [(x, i)]

sorted_key = sorted(position) # y 오름차순 정렬
length = len(sorted_key)
for key in sorted_key: # x 오름차순 정렬
    position[key].sort()

def is_possible(num1, num2):
    return abs(num1 - num2) <= 2

def binary_search(start, end, target, arr, option=0):
    answer = []
    temp_start, temp_end = start, end

    while temp_start <= temp_end:
        mid = (temp_start + temp_end) // 2
        if is_possible(target, arr[mid] if option == 0 else arr[mid][0]):
            temp_end = mid - 1
        else:
            temp_start = mid + 1

    answer.append(temp_start)

    temp_start, temp_end = start, end
    while temp_start <= temp_end:
        mid = (temp_start + temp_end) // 2
        if is_possible(target, arr[mid] if option == 0 else arr[mid][0]):
            temp_start = mid + 1
        else:
            temp_end = mid - 1

    answer.append(temp_start)

    return answer

while heap:
    cnt, target_y, target_x = heappop(heap)
    if target_y == -T:
        print(cnt)
        break
    start, end = binary_search(0, length-1, -target_y, sorted_key)
    cnt += 1

    for i in range(start, end):
        key = sorted_key[i]
        x_list = position[key]
        x_len = len(x_list)

        x_start, x_end = binary_search(0, x_len-1, target_x, x_list, 1)
        for j in range(x_start, x_end):
            x_i = x_list[j][1]
            if visited[x_i] > cnt:
                visited[x_i] = cnt
                heappush(heap, (cnt, -key, x_list[j][0]))

else:
    print(-1)


# 240115
from sys import stdin
from collections import defaultdict, deque
def to_int(): return map(int, stdin.readline().split())

N, T = to_int()
position = []
link_info = [[] for _ in range(N)] # 연결 관계 확인
q = deque() # cnt, y, x
visited = [False] * N
x_limit, y_limit = int(1e6)+1, int(2e5)+1
x_range = defaultdict(set)
y_range = defaultdict(set)
for i in range(N):
    x, y = to_int()
    position.append((x, y))
    x_range[x].add(i)
    y_range[y].add(i)

for i in range(N):
    x, y = position[i]
    x_set, y_set = set(), set()
    for nx in range(max(x-2, 0), min(x+3, x_limit)):
        if x_range.get(nx):
            x_set.update(x_range[nx])

    for ny in range(max(y-2, 0), min(y+3, y_limit)):
        if y_range.get(ny):
            y_set.update(y_range[ny])


    cross = (x_set & y_set) - {i}
    link_info[i].extend(cross)

if y_range.get(T):
    target_set = y_range[T]
    # 출발지에서 갈 수 있는 곳 찾기
    x_set, y_set = set(), set()
    for y in range(3):
        if y_range.get(y):
            y_set.update(y_range[y])

    for x in range(3):
        if x_range.get(x):
            x_set.update(x_range[x])

    cross = x_set & y_set

    for i in cross:
        q.append((1, i))
        visited[i] = True

    while q:
        cnt, i = q.popleft()
        if i in target_set:
            print(cnt)
            break

        cnt += 1
        for j in link_info[i]:
            if not visited[j]:
                q.append((cnt, j))
                visited[j] = True

    else:
        print(-1)

else:
    print(-1)


#
def fill_queue():
    # 출발지에서 갈 수 있는 곳 찾기
    x_set, y_set = set(), set()
    for y in range(3):
        if y_range.get(y):
            y_set.update(y_range[y])

    for x in range(3):
        if x_range.get(x):
            x_set.update(x_range[x])

    cross = x_set & y_set

    for i in cross:
        q.append((1, i))
        visited[i] = True

def bfs():
    if y_range.get(T):
        target_set = y_range[T]
        fill_queue()

        while q:
            cnt, i = q.popleft()
            if i in target_set:
                return cnt

            cnt += 1
            for j in link_info[i]:
                if not visited[j]:
                    q.append((cnt, j))
                    visited[j] = True

        return -1

    return -1

def fill_link_info():
    for i in range(N):
        x, y = position[i]
        x_set, y_set = set(), set()
        for nx in range(max(x - 2, 0), min(x + 3, x_limit)):
            if x_range.get(nx):
                x_set.update(x_range[nx])

        for ny in range(max(y - 2, 0), min(y + 3, y_limit)):
            if y_range.get(ny):
                y_set.update(y_range[ny])

        cross = (x_set & y_set) - {i}
        link_info[i].extend(cross)


from sys import stdin
from collections import defaultdict, deque
def to_int(): return map(int, stdin.readline().split())

N, T = to_int()
position = []
link_info = [[] for _ in range(N)] # 연결 관계 확인
q = deque() # cnt, i
visited = [False] * N
x_limit, y_limit = int(1e6)+1, int(2e5)+1
x_range = defaultdict(set)
y_range = defaultdict(set)
for i in range(N):
    x, y = to_int()
    position.append((x, y))
    x_range[x].add(i)
    y_range[y].add(i)

fill_link_info()

print(bfs())