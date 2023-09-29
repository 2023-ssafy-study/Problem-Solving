#230912

#
N, Q = map(int, input().split())
exponential = [2**i for i in range(7)]
M = exponential[N]
area = [list(map(int, input().split())) for _ in range(M)]
steps = list(map(int, input().split()))

def tornado(length, start_i, start_j):
    if length == L:
        order = []
        for j in range(start_j, start_j + L):
            for i in range(start_i+L-1, start_i-1, -1):
                order.append((i, j))
        index = 0

        for i in range(start_i, start_i+L):
            for j in range(start_j, start_j+L):
                y, x = order[index]
                new_area[i][j] = area[y][x]
                index += 1
        return

    half = length//2
    for di, dj in (0, 0), (0, half), (half, half), (half, 0):
        tornado(half, start_i+di, start_j+dj)

def fire_ball():
    for i in range(M):
        for j in range(M):
            if area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    new_area[i][j] -= 1


for step in steps:
    L = exponential[step]
    new_area = [[0] * M for _ in range(M)]
    tornado(M, 0, 0)
    area = [new_area[i][:] for i in range(M)]
    fire_ball()
    area = [new_area[i][:] for i in range(M)]

def find_sum():
    total = 0
    for i in range(M):
        for j in range(M):
            total += area[i][j]

    return total

def find_cnt():
    from collections import deque
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if not visited[i][j] and area[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if not visited[ny][nx] and area[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

print(find_sum())
print(find_cnt())


#
N, Q = map(int, input().split())
exponential = [2**i for i in range(7)]
M = exponential[N]
area = [list(map(int, input().split())) for _ in range(M)]
steps = list(map(int, input().split()))

def tornado(length, start_i, start_j):
    if length == L:
        order = []
        for j in range(start_j, start_j + L):
            for i in range(start_i+L-1, start_i-1, -1):
                order.append((i, j))
        index = 0

        for i in range(start_i, start_i+L):
            for j in range(start_j, start_j+L):
                y, x = order[index]
                new_area[i][j] = area[y][x]
                index += 1
        return

    half = length//2
    for di, dj in (0, 0), (0, half), (half, half), (half, 0):
        tornado(half, start_i+di, start_j+dj)

def fire_ball():
    for i in range(M):
        for j in range(M):
            if new_area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and new_area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    area[i][j] -= 1


for step in steps:
    L = exponential[step]
    new_area = [[0] * M for _ in range(M)]
    tornado(M, 0, 0)
    area = [new_area[i][:] for i in range(M)]
    fire_ball()

def find_sum():
    total = 0
    for i in range(M):
        for j in range(M):
            total += area[i][j]

    return total

def find_cnt():
    from collections import deque
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if not visited[i][j] and area[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if not visited[ny][nx] and area[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

print(find_sum())
print(find_cnt())


#
def tornado(new_area, area, length, start_i, start_j, L):
    if length == L:
        order = []
        for j in range(start_j, start_j + L):
            for i in range(start_i+L-1, start_i-1, -1):
                order.append((i, j))
        index = 0

        for i in range(start_i, start_i+L):
            for j in range(start_j, start_j+L):
                y, x = order[index]
                new_area[i][j] = area[y][x]
                index += 1
        return

    half = length//2
    for di, dj in (0, 0), (0, half), (half, half), (half, 0):
        tornado(new_area, area, half, start_i+di, start_j+dj, L)

def fire_ball(new_area, area, M):
    for i in range(M):
        for j in range(M):
            if new_area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and new_area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    area[i][j] -= 1

def find_sum(area, M):
    total = 0
    for i in range(M):
        for j in range(M):
            total += area[i][j]

    return total

def find_cnt(area, M):
    from collections import deque
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if not visited[i][j] and area[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if not visited[ny][nx] and area[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

def print_answer():
    N, Q = map(int, input().split())
    exponential = [2**i for i in range(7)]
    M = exponential[N]
    area = [list(map(int, input().split())) for _ in range(M)]
    steps = list(map(int, input().split()))

    for step in steps:
        L = exponential[step]
        new_area = [[0] * M for _ in range(M)]
        tornado(new_area, area, M, 0, 0, L)
        area = [new_area[i][:] for i in range(M)]
        fire_ball(new_area, area, M)

    print(find_sum(area, M))
    print(find_cnt(area, M))

print_answer()


#
def tornado(new_area, area, M, L):
    for i in range(0, M, L):
        for j in range(0, M, L):
            order = []
            for nj in range(j, j + L):
                for ni in range(i+L-1, i-1, -1):
                    order.append((ni, nj))

            index = 0

            for ni in range(i, i + L):
                for nj in range(j, j + L):
                    y, x = order[index]
                    new_area[ni][nj] = area[y][x]
                    index += 1

def fire_ball(new_area, area, M):
    for i in range(M):
        for j in range(M):
            if new_area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and new_area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    area[i][j] -= 1

def find_sum(area, M):
    total = 0
    for i in range(M):
        for j in range(M):
            total += area[i][j]

    return total

def find_cnt(area, M):
    from collections import deque
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if not visited[i][j] and area[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if not visited[ny][nx] and area[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

def print_answer():
    N, Q = map(int, input().split())
    exponential = [2**i for i in range(7)]
    M = exponential[N]
    area = [list(map(int, input().split())) for _ in range(M)]
    steps = list(map(int, input().split()))

    for step in steps:
        L = exponential[step]
        new_area = [[0] * M for _ in range(M)]
        tornado(new_area, area, M, L)
        area = [new_area[i][:] for i in range(M)]
        fire_ball(new_area, area, M)

    print(find_sum(area, M))
    print(find_cnt(area, M))

print_answer()


#
def tornado(new_area, area, M, L):
    for i in range(0, M, L):
        for j in range(0, M, L):
            order = []
            for nj in range(j, j + L):
                for ni in range(i+L-1, i-1, -1):
                    order.append((ni, nj))

            index = 0

            for ni in range(i, i + L):
                for nj in range(j, j + L):
                    y, x = order[index]
                    new_area[ni][nj] = area[y][x]
                    index += 1

def fire_ball(new_area, area, M):
    for i in range(M):
        for j in range(M):
            if new_area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and new_area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    area[i][j] -= 1

def find_sum(area, M):
    total = 0
    for i in range(M):
        for j in range(M):
            total += area[i][j]

    return total

def find_cnt(area, M):
    from collections import deque
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if area[i][j] and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if area[ny][nx] and not visited[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

def print_answer():
    N, Q = map(int, input().split())
    exponential = [2**i for i in range(7)]
    M = exponential[N]
    area = [list(map(int, input().split())) for _ in range(M)]
    steps = list(map(int, input().split()))

    for step in steps:
        L = exponential[step]
        new_area = [[0] * M for _ in range(M)]
        tornado(new_area, area, M, L)
        area = [new_area[i][:] for i in range(M)]
        fire_ball(new_area, area, M)

    print(find_sum(area, M))
    print(find_cnt(area, M))

print_answer()


#
def tornado(new_area, area, M, L):
    for i in range(0, M, L):
        for j in range(0, M, L):
            order = []
            for nj in range(j, j + L):
                for ni in range(i+L-1, i-1, -1):
                    order.append((ni, nj))

            index = 0

            for ni in range(i, i + L):
                for nj in range(j, j + L):
                    y, x = order[index]
                    new_area[ni][nj] = area[y][x]
                    index += 1

def fire_ball(new_area, area, M):
    for i in range(M):
        for j in range(M):
            if new_area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and new_area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    area[i][j] -= 1

def find_sum(area, M):
    total = 0
    for i in range(M):
        for j in range(M):
            total += area[i][j]

    return total

def find_cnt(area, M):
    from collections import deque
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if area[i][j] and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if area[ny][nx] and not visited[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

def print_answer():
    N, Q = map(int, input().split())
    exponential = [2**i for i in range(7)]
    M = exponential[N]
    area = [list(map(int, input().split())) for _ in range(M)]
    steps = list(map(int, input().split()))

    for step in steps:
        L = exponential[step]
        new_area = [[0] * M for _ in range(M)]
        tornado(new_area, area, M, L)
        for i in range(M):
            for j in range(M):
                area[i][j] = new_area[i][j]
        fire_ball(new_area, area, M)

    print(find_sum(area, M))
    print(find_cnt(area, M))

print_answer()


#
def tornado(new_area, area, M, L):
    for i in range(0, M, L):
        for j in range(0, M, L):
            order = []
            for nj in range(j, j + L):
                for ni in range(i+L-1, i-1, -1):
                    order.append((ni, nj))

            index = 0

            for ni in range(i, i + L):
                for nj in range(j, j + L):
                    y, x = order[index]
                    new_area[ni][nj] = area[y][x]
                    index += 1

def fire_ball(new_area, area, M):
    for i in range(M):
        for j in range(M):
            if new_area[i][j]:
                cnt = 0
                for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < M and 0 <= nj < M and new_area[ni][nj]:
                        cnt += 1
                if cnt < 3:
                    area[i][j] -= 1

def find_sum_cnt(area, M):
    from collections import deque
    max_cnt = total = 0
    visited = [[False] * M for _ in range(M)]
    q = deque()
    for i in range(M):
        for j in range(M):
            if area[i][j] and not visited[i][j]:
                total += area[i][j]
                q.append((i, j))
                visited[i][j] = True
                cnt = 1
                while q:
                    y, x = q.popleft()
                    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < M and 0 <= nx < M:
                            if area[ny][nx] and not visited[ny][nx]:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                                total += area[ny][nx]
                if cnt > max_cnt:
                    max_cnt = cnt
    return total, max_cnt

def print_answer():
    N, Q = map(int, input().split())
    exponential = [2**i for i in range(7)]
    M = exponential[N]
    area = [list(map(int, input().split())) for _ in range(M)]
    steps = list(map(int, input().split()))

    for step in steps:
        L = exponential[step]
        new_area = [[0] * M for _ in range(M)]
        tornado(new_area, area, M, L)
        area = [new_area[i][:] for i in range(M)]
        fire_ball(new_area, area, M)

    print(*find_sum_cnt(area, M), sep='\n')

print_answer()