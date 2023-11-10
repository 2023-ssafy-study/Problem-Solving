import sys

input = sys.stdin.readline

N = int(input())
edges = []
degrees = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
    degrees[u] += 1
    degrees[v] += 1

cnt_d = 0  # 정점을 기준으로 연결된 노드가 3개 이상일 때 3개를 선택하는 경우 계산해 더하기
cnt_g = 0  # 한 간선을 구성하고 있는 두 정점에 연결된 정점의 수 곱해서 더하기

for v in range(1, N + 1):
    cnt_g += degrees[v] * (degrees[v] - 1) * (degrees[v] - 2) / 6 if degrees[v] >= 3 else 0
for u, v in edges:
    cnt_d += (degrees[u] - 1) * (degrees[v] - 1)

if cnt_d > cnt_g * 3:
    print('D')
elif cnt_d < cnt_g * 3:
    print('G')
else:
    print('DUDUDUNGA')
