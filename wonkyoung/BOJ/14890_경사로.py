# 230908
N, L = map(int, input().split()) # 지도의 크기 (가로, 세로), 경사로 길이
map_info = [list(map(int, input().split())) for _ in range(N)] # 지도 정보
road = 0 # 길의 개수

# 행 탐색
for i in range(N):
    conseq = 1 # 연속된 숫자 개수
    after_count = False # 이 이후에 경사로를 놓을지 여부
    before = map_info[i][0] # 연속된 숫자
    for j in range(1, N):
        area = map_info[i][j]
        if area == before: # 숫자가 연속될 때
            conseq += 1
        else:
            if area == before - 1: # 앞 > 뒤 - 뒤에 경사로를 놓아야 함
                if after_count and conseq < L: # 여기에 경사로를 놓아야 하는데 길이 조건 충족 X
                    break
                after_count = True
            elif area == before + 1 and conseq >= L: # 앞 < 뒤 - 앞에 경사로를 놓아야 함
                if after_count and conseq < 2 * L: # 여기에 경사로를 놓아야 하는데 길이 조건 충족 X
                    break
                after_count = False
            else:
                break

            conseq = 1
            before = area
    else:
        if not after_count or conseq >= L: # 현재 경사로를 놓지 않아도 되거나, 경사로 길이보다 연속된 부분 길이 클 때
            road += 1

# 열 탐색
for j in range(N):
    conseq = 1
    after_count = False
    before = map_info[0][j]
    for i in range(1, N):
        area = map_info[i][j]
        if area == before:
            conseq += 1
        else:
            if area == before - 1:
                if after_count and conseq < L:
                    break
                after_count = True
            elif area == before + 1 and conseq >= L:
                if after_count and conseq < 2*L:
                    break
                after_count = False
            else:
                break
            conseq = 1
            before = area
    else:
        if not after_count or conseq >= L:
            road += 1


print(road)


#
def cnt_road(N, L, map_info):
    road = 0
    for option in range(2):
        for i in range(N):
            conseq = 1
            after_count = False
            before = map_info[i][0] if option == 0 else map_info[0][i]
            for j in range(1, N):
                area = map_info[i][j] if option == 0 else map_info[j][i]
                if area == before:
                    conseq += 1
                else:
                    if area == before - 1:
                        if after_count and conseq < L:
                            break
                        after_count = True
                    elif area == before + 1 and conseq >= L:
                        if after_count and conseq < 2 * L:
                            break
                        after_count = False
                    else:
                        break

                    conseq = 1
                    before = area
            else:
                if not after_count or conseq >= L:
                    road += 1

    return road


N, L = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]

print(cnt_road(N, L, map_info))