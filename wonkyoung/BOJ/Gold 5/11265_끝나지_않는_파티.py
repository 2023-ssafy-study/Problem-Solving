# 240722
# 34320 KB / 2784 ms
from sys import stdin

def int_input():
    return map(int, stdin.readline().split())

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if j != k:
                        new_path = time_table[i][k] + time_table[k][j]
                        if time_table[i][j] > new_path:
                            time_table[i][j] = new_path

def can_arrive(now, target, limit):
    if time_table[now-1][target-1] <= limit:
        return 'Enjoy other party'
    return 'Stay here'

N, M = int_input()
time_table = [list(int_input()) for _ in range(N)]
floyd_warshall()

for _ in range(M):
    print(can_arrive(*int_input()))




# 34320 KB / 2520 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    def floyd_warshall():
        for k in range(N):
            for i in range(N):
                if i != k:
                    for j in range(N):
                        if j != k:
                            new_path = time_table[i][k] + time_table[k][j]
                            if time_table[i][j] > new_path:
                                time_table[i][j] = new_path

    def can_arrive(now, target, limit):
        if time_table[now - 1][target - 1] <= limit:
            return 'Enjoy other party'
        return 'Stay here'

    N, M = int_input()
    time_table = [list(int_input()) for _ in range(N)]
    floyd_warshall()

    for _ in range(M):
        print(can_arrive(*int_input()))

main()