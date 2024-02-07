from sys import stdin

input = stdin.readline

N, T = map(int, input().split())
time = [0] * 100001
max_E = 0
for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        time[S] += 1
        time[E] -= 1
        max_E = max(max_E, E)

for i in range(1, max_E + 1):
    time[i] += time[i - 1]

max_s, s = 0, 0
answer = 0
l, r = 0, T - 1
for t in range(l, r + 1):
    s += time[t]

while r < max_E:
    if s > max_s:
        max_s = s
        answer = l
    s -= time[l]
    l += 1
    r += 1
    s += time[r]

print(answer, answer + T)
