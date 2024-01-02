import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def find_depths(v, d):  # 현재 노드에서 루트까지의 거리 측정
    if par[v] == 0:
        return d
    return find_depths(par[v], d + 1)


T = int(input())
for _ in range(T):
    N = int(input())  # 트리를 구성하는 노드의 수
    par = [0] * (N + 1)  # i노드의 부모 저장
    for _ in range(N - 1):
        A, B = map(int, input().split())  # A가 B의 부모
        par[B] = A

    v1, v2 = map(int, input().split())
    d1, d2 = find_depths(v1, 0), find_depths(v2, 0)

    while d1 != d2:  # depths를 맞춘다
        if d1 > d2:
            v1, d1 = par[v1], d1 - 1
        elif d1 < d2:
            v2, d2 = par[v2], d2 - 1

    while v1 != v2:
        v1, v2 = par[v1], par[v2]

    print(v1)
