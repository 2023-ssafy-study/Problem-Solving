from math import ceil, log
N, M, K = map(int, input().split())
h = ceil(log(N, 2))
tree = [0] * (2 ** (h+1))
for i in range(N):
    tree[2 ** h + i] = int(input())

def make_top_down(n):
    global tree
    if n >= (2**h):
        return tree[n]
    tree[n] = make_top_down(n*2) + make_top_down(n*2+1)
    return tree[n]
make_top_down(1)

def make_bot_up():
    global tree
    for i in range(2**h-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]
#make_bot_up()
def change(b, c):
    # 리프노드부터 그 부모노드에 차이를 더해준다.
    leaf = 2**h + b - 1
    diff = c - tree[leaf]
    # 부모노드 : leaf를 2로 나눈 몫
    par = leaf
    while par > 0:
        tree[par] += diff
        par //= 2
def solve(l, r, node): # l, r은 해당범위
    if b <= l and r <= c:
        # 탐색범위가 해당범위에 들어가면(작으면)
        # 3 <= (3, 4) <= 5
        return tree[node]
    if r < b or c < l:
        # 탐색범위가 해당범위 바깥이면
        # (1, 1) < 2, 5 < (7, 8)
        return 0
    # 탐색범위가 해당범위보다 크거나, 겹치면
    # 이진탐색처럼 l, r 범위를 줄인다.
    mid = (l + r) // 2
    return solve(l, mid, node*2) + solve(mid+1, r, node*2+1) #우측탐색 + 좌측탐색

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        change(b, c)
    else:
        # (b, c) 해당범위
        # 바닥노드를 제외한 노드만 탐색
        ret = solve(1, 2**h, 1)
        print(ret)