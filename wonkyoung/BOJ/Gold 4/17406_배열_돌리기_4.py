# 231010
N, M, K = map(int, input().split())
# 배열
arr =[[0] * M] + [[0] + list(map(int, input().split())) for _ in range(N)]
# 회전 연산 목록
order_list = [list(map(int, input().split())) for _ in range(K)]
visited = [False] * K
min_total = 6000

def rotate_arr(r, c, s):
    temp_arr = [[0] * (M+1) for _ in range(N+1)]
    temp_arr[r][c] = arr[r][c]

    for num in range(s):

        for j in range(c-s+num+1, c+s-num+1):
            top, bottom = r-s+num, r+s-num
            # 위쪽 (오른쪽으로 이동)
            temp_arr[top][j] = arr[top][j-1]
            # 아래쪽 (왼쪽으로 이동)
            temp_arr[bottom][j-1] = arr[bottom][j]

        for i in range(r - s + num, r + s - num):
            left, right = c - s + num, c + s - num
            # 오른쪽 (아래로 이동)
            temp_arr[i+1][right] = arr[i][right]
            # 왼쪽 (위로 이동)
            temp_arr[i][left] = arr[i+1][left]

    for i in range(r-s, r+s+1):
        for j in range(c-s, c+s+1):
            arr[i][j] = temp_arr[i][j]


# 회전 순서 결정
def determine_order(level=0):
    global min_total
    if level == K:
        for i in range(1, N+1):
            total = sum(arr[i])
            if total < min_total:
                min_total = total
        return

    for index in range(K):
        if not visited[index]:
            visited[index] = True
            before_arr = [arr[i][:] for i in range(N+1)]

            rotate_arr(*order_list[index])
            determine_order(level+1)

            visited[index] = False
            for i in range(1, N+1):
                for j in range(1, M+1):
                    arr[i][j] = before_arr[i][j]

determine_order()
print(min_total)


#
N, M, K = map(int, input().split())
# 배열
arr =[[0] * M] + [[0] + list(map(int, input().split())) for _ in range(N)]
# 회전 연산 목록
order_list = [list(map(int, input().split())) for _ in range(K)]
visited = [False] * K
min_total = 6000

def rotate_arr(r, c, s):
    temp_arr = [[0] * (M+1) for _ in range(N+1)]
    temp_arr[r][c] = arr[r][c]

    for num in range(s):

        for j in range(c-s+num+1, c+s-num+1):
            top, bottom = r-s+num, r+s-num
            # 위쪽 (오른쪽으로 이동)
            temp_arr[top][j] = arr[top][j-1]
            # 아래쪽 (왼쪽으로 이동)
            temp_arr[bottom][j-1] = arr[bottom][j]

        for i in range(r - s + num, r + s - num):
            left, right = c - s + num, c + s - num
            # 오른쪽 (아래로 이동)
            temp_arr[i+1][right] = arr[i][right]
            # 왼쪽 (위로 이동)
            temp_arr[i][left] = arr[i+1][left]

    for i in range(r-s, r+s+1):
        for j in range(c-s, c+s+1):
            arr[i][j] = temp_arr[i][j]


# 회전 순서 결정
def determine_order(level=0):
    global min_total
    if level == K:
        for i in range(1, N+1):
            total = sum(arr[i])
            if total < min_total:
                min_total = total
        return

    for index in range(K):
        if not visited[index]:
            visited[index] = True
            before_arr = [arr[i][:] for i in range(N+1)]
            r, c, s = order_list[index]
            rotate_arr(r, c, s)
            determine_order(level+1)

            visited[index] = False
            for i in range(r-s, r+s+1):
                for j in range(c-s, c+s+1):
                    arr[i][j] = before_arr[i][j]

determine_order()
print(min_total)


#
def find_min_total():
    # 배열 회전
    def rotate_arr(r, c, s):
        temp_arr = [[0] * (M + 1) for _ in range(N + 1)]
        temp_arr[r][c] = arr[r][c]

        for num in range(s):

            for j in range(c - s + num + 1, c + s - num + 1):
                top, bottom = r - s + num, r + s - num
                # 위쪽 (오른쪽으로 이동)
                temp_arr[top][j] = arr[top][j - 1]
                # 아래쪽 (왼쪽으로 이동)
                temp_arr[bottom][j - 1] = arr[bottom][j]

            for i in range(r - s + num, r + s - num):
                left, right = c - s + num, c + s - num
                # 오른쪽 (아래로 이동)
                temp_arr[i + 1][right] = arr[i][right]
                # 왼쪽 (위로 이동)
                temp_arr[i][left] = arr[i + 1][left]

        for i in range(r - s, r + s + 1):
            for j in range(c - s, c + s + 1):
                arr[i][j] = temp_arr[i][j]

    # 회전 순서 결정
    def determine_order(level=0):
        nonlocal min_total
        if level == K:
            for i in range(1, N + 1):
                total = sum(arr[i])
                if total < min_total:
                    min_total = total
            return

        for index in range(K):
            if not visited[index]:
                visited[index] = True
                before_arr = [arr[i][:] for i in range(N + 1)]
                r, c, s = order_list[index]
                rotate_arr(r, c, s)
                determine_order(level + 1)

                visited[index] = False
                for i in range(r - s, r + s + 1):
                    for j in range(c - s, c + s + 1):
                        arr[i][j] = before_arr[i][j]


    N, M, K = map(int, input().split())
    # 배열
    arr =[[0] * M] + [[0] + list(map(int, input().split())) for _ in range(N)]
    # 회전 연산 목록
    order_list = [list(map(int, input().split())) for _ in range(K)]
    visited = [False] * K # 연산 실행 여부
    min_total = 6000 # 행 합의 최솟값

    determine_order()

    return min_total

print(find_min_total())