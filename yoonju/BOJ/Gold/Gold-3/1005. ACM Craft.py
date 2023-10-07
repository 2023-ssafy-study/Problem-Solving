# 252196 KB 480 ms (PyPy3)
# 43940 KB 824 ms (Python3)

import sys

sys.setrecursionlimit(10**5)

def cal_min_time():
    def find_value(index):
        # 방문한 적 있으면 DP[index] 리턴
        if DP[index] > -1:
            return DP[index]
        # index가 sequence에 존재하지 않으면 딜레이 시간 리턴
        # ex) 맨 처음 시작점 (1)
        if index not in sequence:
            return spend_time[index]

        # index를 짓기 전 선행되어야 하는 건물들을 차례로 확인
        for seq in sequence[index]:
            res = find_value(seq)
            # 건물 A까지 짓는데 걸리는 시간이 DP[index] 보다 크면 교체
            if DP[index] < res:
                DP[index] = res

        # DP[index]에 index 건물 짓는데 걸리는 시간 더하기
        DP[index] += spend_time[index]
        return DP[index]

    n, k = map(int, sys.stdin.readline().split())
    spend_time = [0] + list(map(int, sys.stdin.readline().split()))

    DP = [-1]*(n+1)

    sequence = {}

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        # 후행 건설되는 건물을 key로 잡기
        if y not in sequence:
            sequence[y] = []
        sequence[y].append(x)

    w = int(sys.stdin.readline())

    print(find_value(w))

t = int(sys.stdin.readline())

for _ in range(t):
    cal_min_time()