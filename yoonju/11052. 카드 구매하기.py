# 31256 KB 132 ms

import sys

N = int(sys.stdin.readline())

P = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    # N => N vs i + N-i
    for j in range(i+1, N+1):
        if P[i] + P[j-i] > P[j]:
            P[j] = P[i] + P[j-i]

print(P[N])