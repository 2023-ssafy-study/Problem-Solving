from copy import deepcopy

# 얼음 위치 탐색
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 90도회전함수
def Rotate_ninty(R_ice):
    global len_ice
    for i in range(0, len_ice, R_ice):
        for j in range(0, len_ice, R_ice):
            for k in range(R_ice):
                for p in range(R_ice):
                    temp_ice[i + k][j + R_ice - p - 1] = ice[i + p][j + k]
    return


# 얼음을 비교해서 녹일 함수
def meltingice(temp_ice):
    global len_ice
    temp_w = []
    for i in range(len_ice):
        for j in range(len_ice):
            temp_count = 0
            for di, dj in direct:
                ni = i + di
                nj = j + dj
                if (0 <= ni < len_ice) and (0 <= nj < len_ice):
                    if temp_ice[ni][nj] > 0:
                        temp_count += 1

            if temp_count < 3 and temp_ice[i][j] > 0:
                temp_w.append((i, j))

    for ni, nj in temp_w:
        temp_ice[ni][nj] -= 1

# 얼음전체 크기와 가장큰 얼음
def Count_ice(temp_ice):
    # 방문 기록
    visit_ice = [[0] * len_ice for _ in range(len_ice)]
    # BFS할 큐의 시작과 헤드
    q_s = -1
    q_h = -1
    q = []
    # 가장큰 얼음섬과 전체 합
    ans_max_ice = 0
    all_ice = 0
    for i in range(len_ice):
        for j in range(len_ice):
            max_ice = 0
            all_ice += temp_ice[i][j]
            if temp_ice[i][j] > 0 and visit_ice[i][j] == 0:
                max_ice += 1
                visit_ice[i][j] = 1
                for di, dj in direct:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < len_ice and 0 <= nj < len_ice and temp_ice[ni][nj] > 0 and visit_ice[ni][nj] == 0:
                        q.append((ni, nj))
                        visit_ice[ni][nj] += 1
                        q_h += 1
                while q_s < q_h:
                    q_s += 1
                    i2, j2 = q[q_s]
                    max_ice += 1
                    for di, dj in direct:
                        ni2 = i2 + di
                        nj2 = j2 + dj
                        if 0 <= ni2 < len_ice and 0 <= nj2 < len_ice and temp_ice[ni2][nj2] > 0 and visit_ice[ni2][
                            nj2] == 0:
                            q.append((ni2, nj2))
                            q_h += 1
                            visit_ice[ni2][nj2] += 1

            ans_max_ice = max(ans_max_ice, max_ice)
    return all_ice, ans_max_ice


# 시작 좌표, 격자 길이

N, Q = map(int, input().split())
len_ice = 2 ** N

ice = [list(map(int, input().split())) for _ in range(len_ice)]
Ls = list(map(int, input().split()))

# 회전한것을 저장할 배열
temp_ice = [[0] * len_ice for _ in range(len_ice)]

# 회전할 for 문
for l in Ls:
    Rotate_ninty(2 ** l)
    meltingice(temp_ice)
    ice = deepcopy(temp_ice)

print(*Count_ice(ice))
