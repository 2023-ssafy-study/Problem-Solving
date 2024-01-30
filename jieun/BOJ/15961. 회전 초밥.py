import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

l, r = 0, k - 1
eat = {}
eat[c] = 1
for i in range(l, r + 1):
    eat[sushi[i]] = eat.get(sushi[i], 0) + 1
answer = len(eat)

while l < N:
    if eat[sushi[l]] == 1:
        del eat[sushi[l]]
    else:
        eat[sushi[l]] -= 1
    l += 1
    r += 1
    eat[sushi[r % N]] = eat.get(sushi[r % N], 0) + 1
    answer = max(answer, len(eat))

print(answer)
