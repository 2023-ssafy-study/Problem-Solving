# 31120 KB / 748 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    tc = int(new_input())
    max_time = 2.6e7

    def bellman_ford():
        total_time = [max_time] * (N + 1)
        total_time[1] = 0
        for _ in range(N-1):
            for new_s, new_e, time in road:
                if total_time[new_e] > total_time[new_s] + time:
                    total_time[new_e] = total_time[new_s] + time

        for new_s, new_e, time in road:
            if total_time[new_e] > total_time[new_s] + time:
                return 'YES'

        return 'NO'


    for i in range(tc):
        N, M, W = map(int, new_input().split())
        road = []

        for _ in range(M):
            s, e, time = map(int, new_input().split())
            road.append((s, e, time))
            road.append((e, s, time))

        for _ in range(W):
            s, e, time = map(int, new_input().split())
            road.append((s, e, -time))

        print(bellman_ford())

main()