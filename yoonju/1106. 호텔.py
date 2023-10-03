# 31256 KB 160 ms

import sys

c, n = map(int, sys.stdin.readline().split())

# 비용과 얻을 수 있는 고객의 수는 100보다 작거나 같은 자연수!
consumers = [2e9]*(c+101)

for _ in range(n):
    cost, consumer_cnt = map(int, sys.stdin.readline().split())
    consumers[consumer_cnt] = min(consumers[consumer_cnt], cost)

for i in range(2, c+101):
    for j in range(1, i//2+1):
        consumers[i] = min(consumers[i], consumers[i-j] + consumers[j])

print(min(consumers[c:]))