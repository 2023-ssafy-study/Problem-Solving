#230926
N = int(input())
length = [1] + [2**i for i in range(10)]
direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dots = set()
cnt = 0
for _ in range(N):
    x, y, d, g = map(int, input().split())
    nx, ny, nd = x+direct[d][0], y+direct[d][1], (d+1)%4
    dragon_curve = [(x, y, d), (nx, ny, nd)]
    if 0 <= x <= 100 and 0 <= y <= 100:
        dots.add((x, y))
    if 0 <= nx <= 100 and 0 <= ny <= 100:
        dots.add((nx, ny))
    for i in range(1, g+1):
        ref_x, ref_y = dragon_curve[-1][:2]
        for j in range(length[i]-1, -1, -1):
            ref_d = dragon_curve[j+1][2]
            nx, ny, nd = ref_x+direct[ref_d][0], ref_y+direct[ref_d][1], (ref_d+1)%4
            dragon_curve.append((nx, ny, nd))
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                dots.add((nx, ny))
            ref_x, ref_y = nx, ny

if dots:
    for j in range(100):
        for i in range(100):
            for ni, nj in (i, j), (i+1, j), (i, j+1), (i+1, j+1):
                if (nj, ni) not in dots:
                    break
            else:
                cnt += 1

print(cnt)


#
N = int(input())
length = [1] + [2**i for i in range(10)]
direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dots = set()
cnt = 0
for _ in range(N):
    x, y, d, g = map(int, input().split())
    nx, ny, nd = x+direct[d][0], y+direct[d][1], (d+1)%4
    dragon_curve = [(x, y, d), (nx, ny, nd)]
    if 0 <= x <= 100 and 0 <= y <= 100:
        dots.add((x, y))
    if 0 <= nx <= 100 and 0 <= ny <= 100:
        dots.add((nx, ny))
    for i in range(1, g+1):
        ref_x, ref_y, ref_d = dragon_curve[-1]
        for j in range(length[i]-1, -1, -1):
            nx, ny, nd = ref_x+direct[ref_d][0], ref_y+direct[ref_d][1], (ref_d+1)%4
            dragon_curve.append((nx, ny, nd))
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                dots.add((nx, ny))
            ref_x, ref_y = nx, ny
            ref_d = dragon_curve[j][2]

if dots:
    for j in range(100):
        for i in range(100):
            for ni, nj in (i, j), (i+1, j), (i, j+1), (i+1, j+1):
                if (nj, ni) not in dots:
                    break
            else:
                cnt += 1

print(cnt)


#
N = int(input())
length = [1] + [2**i for i in range(10)]
direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dots = set()
cnt = 0
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve = [(x, y, d)]
    if 0 <= x <= 100 and 0 <= y <= 100:
        dots.add((x, y))
    for i in range(g+1):
        ref_x, ref_y, ref_d = dragon_curve[-1]
        for j in range(length[i]-1, -1, -1):
            nx, ny, nd = ref_x+direct[ref_d][0], ref_y+direct[ref_d][1], (ref_d+1)%4
            dragon_curve.append((nx, ny, nd))
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                dots.add((nx, ny))
            ref_x, ref_y = nx, ny
            ref_d = dragon_curve[j][2]

if dots:
    for j in range(100):
        for i in range(100):
            for ni, nj in (i, j), (i+1, j), (i, j+1), (i+1, j+1):
                if (nj, ni) not in dots:
                    break
            else:
                cnt += 1

print(cnt)


#
N = int(input())
length = [0] + [2**i - 1 for i in range(10)]
direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dots = set()
cnt = 0
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve = [(x, y, d)]
    if 0 <= x <= 100 and 0 <= y <= 100:
        dots.add((x, y))
    for i in range(g+1):
        ref_x, ref_y, ref_d = dragon_curve[-1]
        for j in range(length[i], -1, -1):
            nx, ny, nd = ref_x+direct[ref_d][0], ref_y+direct[ref_d][1], (ref_d+1)%4
            dragon_curve.append((nx, ny, nd))
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                dots.add((nx, ny))
            ref_x, ref_y = nx, ny
            ref_d = dragon_curve[j][2]

if dots:
    for j in range(100):
        for i in range(100):
            for ni, nj in (i, j), (i+1, j), (i, j+1), (i+1, j+1):
                if (nj, ni) not in dots:
                    break
            else:
                cnt += 1

print(cnt)


#
def has_square(dots):
    cnt = 0
    if dots:
        for j in range(100):
            for i in range(100):
                for ni, nj in (i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1):
                    if (nj, ni) not in dots:
                        break
                else:
                    cnt += 1

    return cnt

def find_square_cnt():
    N = int(input())
    length = [0] + [2**i - 1 for i in range(10)]
    direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dots = set()

    for _ in range(N):
        x, y, d, g = map(int, input().split())
        dragon_curve = [(x, y, d)]
        if 0 <= x <= 100 and 0 <= y <= 100:
            dots.add((x, y))
        for i in range(g+1):
            ref_x, ref_y, ref_d = dragon_curve[-1]
            for j in range(length[i], -1, -1):
                nx, ny, nd = ref_x+direct[ref_d][0], ref_y+direct[ref_d][1], (ref_d+1)%4
                dragon_curve.append((nx, ny, nd))
                if 0 <= nx <= 100 and 0 <= ny <= 100:
                    dots.add((nx, ny))
                ref_x, ref_y = nx, ny
                ref_d = dragon_curve[j][2]

    return has_square(dots)

print(find_square_cnt())


#
def has_square(visited):
    cnt = 0
    for j in range(100):
        for i in range(100):
            for ni, nj in (i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1):
                if not visited[ni][nj]:
                    break
            else:
                cnt += 1

    return cnt

def find_square_cnt():
    N = int(input())
    length = [0] + [2**i - 1 for i in range(10)]
    direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    visited = [[False] * 101 for _ in range(101)]

    for _ in range(N):
        x, y, d, g = map(int, input().split())
        dragon_curve = [(x, y, d)]
        if 0 <= x <= 100 and 0 <= y <= 100 and not visited[y][x]:
            visited[y][x] = True
        for i in range(g+1):
            ref_x, ref_y, ref_d = dragon_curve[-1]
            for j in range(length[i], -1, -1):
                nx, ny, nd = ref_x+direct[ref_d][0], ref_y+direct[ref_d][1], (ref_d+1)%4
                dragon_curve.append((nx, ny, nd))
                if 0 <= nx <= 100 and 0 <= ny <= 100 and not visited[ny][nx]:
                    visited[ny][nx] = True
                ref_x, ref_y = nx, ny
                ref_d = dragon_curve[j][2]

    return has_square(visited)

print(find_square_cnt())