import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = map(int, input().split())

ps = 0  # 현재까지의 누적합
answer = 0
ps_dict = {0: 1}  # 딕셔너리에 누적합을 저장한다(값:개수)
for a in A:
    ps += a
    if ps - K in ps_dict.keys():
        answer += ps_dict[ps - K]
    ps_dict[ps] = ps_dict.get(ps, 0) + 1

print(answer)
