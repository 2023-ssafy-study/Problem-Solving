from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
ss = [input() for _ in range(N)]

answer = 0
length = {}  # 이름 길이: 학생 수

# 반 등수 차이 <= K && 이름 길이 같은 친구
for i in range(N):
    if i - K > 0: length[len(ss[i - K - 1])] -= 1
    answer += length.get(len(ss[i]), 0)
    length[len(ss[i])] = length.get(len(ss[i]), 0) + 1

print(answer)
