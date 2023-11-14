N = int(input())
scores = [int(input()) for _ in range(N)]
answer = 0

for i in range(N - 1, 0, -1):
    if scores[i - 1] < scores[i]:   continue
    answer += scores[i - 1] - scores[i] + 1
    scores[i - 1] = scores[i] - 1

print(answer)
