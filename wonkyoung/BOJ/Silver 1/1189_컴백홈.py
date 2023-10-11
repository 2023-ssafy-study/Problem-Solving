#231011
R, C, K = map(int, input().split())
impossible_cnt = 0
map_info = []

for _ in range(R):
    map_info.append(input())
    for j in range(C):
        if map_info[-1][j] == 'T':
            impossible_cnt += 1

if K > R*C-impossible_cnt:
    print(0)
else:
    visited = [[False] * C for _ in range(R)]
    cnt = 0

    def cnt_path(y=R-1, x=0, level=1):
        global cnt
        if level == K:
            if y == 0 and x == C-1:
                cnt += 1
                return
            return

        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and map_info[ny][nx] == '.':
                    visited[ny][nx] = True
                    cnt_path(ny, nx, level+1)
                    visited[ny][nx] = False

    visited[R-1][0] = True
    cnt_path()
    print(cnt)


#
def find_path_cnt():
    R, C, K = map(int, input().split())
    impossible_cnt = 0
    map_info = []

    for _ in range(R):
        map_info.append(input())
        for j in range(C):
            if map_info[-1][j] == 'T':
                impossible_cnt += 1

    if K > R*C-impossible_cnt:
        return 0

    visited = [[False] * C for _ in range(R)]
    cnt = 0

    def cnt_path(y=R-1, x=0, level=1):
        nonlocal cnt
        if level == K:
            if y == 0 and x == C-1:
                cnt += 1
                return
            return

        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and map_info[ny][nx] == '.':
                    visited[ny][nx] = True
                    cnt_path(ny, nx, level+1)
                    visited[ny][nx] = False

    visited[R-1][0] = True
    cnt_path()
    return cnt

print(find_path_cnt())


#
R, C, K = map(int, input().split())
cnt = 0
map_info = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def cnt_path(y=R-1, x=0, level=1):
    global cnt
    if level == K:
        if y == 0 and x == C-1:
            cnt += 1
            return
        return

    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y+dy, x+dx
        if 0 <= ny < R and 0 <= nx < C:
            if not visited[ny][nx] and map_info[ny][nx] == '.':
                visited[ny][nx] = True
                cnt_path(ny, nx, level+1)
                visited[ny][nx] = False

visited[R-1][0] = True
cnt_path()
print(cnt)
