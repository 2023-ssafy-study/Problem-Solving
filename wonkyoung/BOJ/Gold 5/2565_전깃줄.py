# 240207
# 31120 KB / 44ms
N = int(input())
linked_info = [tuple(map(int, input().split())) for _ in range(N)]
a_limit = b_limit = 0
linked_info.sort()
# 전깃줄 잘랐을 때와 전깃줄 자르지 않았을 때의 최대 전선 수
check = [[0, 1] for _ in range(N)]

for i in range(1, N):
    # 전깃줄 잘랐을 때 = 그 전 기준 최대
    check[i][0] = max(check[i-1])
    # 자르지 않았을 때 = 서로 교차하지 않는 전선 최대
    max_val = 0
    b = linked_info[i][1]
    for j in range(i):
        if linked_info[j][1] < b:
            max_val = max(max_val, check[j][1])
    check[i][1] += max_val

print(N - max(check[-1]))




