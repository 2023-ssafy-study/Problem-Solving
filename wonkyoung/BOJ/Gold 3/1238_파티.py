# 230108
# 34212 KB / 60 ms
from sys import stdin
from heapq import heappush, heappop
def to_int(): return map(int, stdin.readline().split())

N, M, X = to_int()
road_list1 = [[] for _ in range(N+1)] # 도시별 길(도착지, 시간) 목록
road_list2 = [[] for _ in range(N+1)] # 도시별 길(출발지, 시간) 목록
limit = int(1e5)
to_x = [limit] * (N+1) # 학생별 x까지 가는 데 걸리는 시간
from_x = [limit] * (N+1) # 학생별 x에서 오는 데 걸리는 시간

for _ in range(M):
    start, end, period = to_int()
    road_list1[start].append((period, end))
    road_list2[end].append((period, start))

to_x[X] = from_x[X] = 0
heap = [(0, X)]

# X에서 다른 도시로
while heap:
    period, end = heappop(heap)
    if period <= from_x[end]:
        for new_period, new_end in road_list1[end]:
            total_period = from_x[end] + new_period
            if total_period < from_x[new_end]:
                from_x[new_end] = total_period
                heappush(heap, (total_period, new_end))

heappush(heap, (0, X))
# 다른 도시에서 X로
while heap:
    period, start = heappop(heap)
    if period <= to_x[start]:
        for new_period, new_start in road_list2[start]:
            total_period = to_x[start] + new_period
            if total_period < to_x[new_start]:
                to_x[new_start] = total_period
                heappush(heap, (total_period, new_start))

max_time = from_x[1] + to_x[1]
for i in range(2, N+1):
    new_time = from_x[i] + to_x[i]
    if new_time > max_time:
        max_time = new_time

print(max_time)



# 34212 KB / 64 ms
from sys import stdin
from heapq import heappush, heappop
def to_int(): return map(int, stdin.readline().split())

N, M, X = to_int()
road_list = [[[] for _ in range(2)] for _ in range(N+1)] # 도시별 길(도착지 또는 출발지, 시간) 목록
limit = int(1e5)
to_from_x = [[limit] * 2 for _ in range(N+1)] # 학생별 x까지 오는/가는 데 걸리는 시간

for _ in range(M):
    start, end, period = to_int()
    road_list[start][0].append((period, end))
    road_list[end][1].append((period, start))

to_from_x[X] = [0] * 2
heap = []

for i in range(2):
    heappush(heap, (0, X))
    while heap:
        period, city = heappop(heap)
        if period <= to_from_x[city][i]:
            for new_period, new_city in road_list[city][i]:
                total_period = to_from_x[city][i] + new_period
                if total_period < to_from_x[new_city][i]:
                    to_from_x[new_city][i] = total_period
                    heappush(heap, (total_period, new_city))

max_time = sum(to_from_x[1])
for i in range(2, N+1):
    new_time = sum(to_from_x[i])
    if new_time > max_time:
        max_time = new_time

print(max_time)



# 34256 KB / 60 ms

def fill_arr(road_list, arr, X):
    from heapq import heappush, heappop
    arr[X] = 0
    heap = [(0, X)]

    while heap:
        period, city = heappop(heap)
        if period <= arr[city]:
            for new_period, new_city in road_list[city]:
                total_period = arr[city] + new_period
                if total_period < arr[new_city]:
                    arr[new_city] = total_period
                    heappush(heap, (total_period, new_city))

def find_max_sum(arr1, arr2, N):
    max_time = arr1[1] + arr2[1]
    for i in range(2, N + 1):
        new_time = arr1[i] + arr2[i]
        if new_time > max_time:
            max_time = new_time

    return max_time


def main():
    from sys import stdin
    def to_int(): return map(int, stdin.readline().split())

    N, M, X = to_int()
    road_list1 = [[] for _ in range(N + 1)]  # 도시별 길(도착지, 시간) 목록
    road_list2 = [[] for _ in range(N + 1)]  # 도시별 길(출발지, 시간) 목록
    limit = int(1e5)
    to_x = [limit] * (N + 1)  # 학생별 x까지 가는 데 걸리는 시간
    from_x = [limit] * (N + 1)  # 학생별 x에서 오는 데 걸리는 시간

    for _ in range(M):
        start, end, period = to_int()
        road_list1[start].append((period, end))
        road_list2[end].append((period, start))


    fill_arr(road_list1, from_x, X)
    fill_arr(road_list2, to_x, X)

    print(find_max_sum(from_x, to_x, N))


main()