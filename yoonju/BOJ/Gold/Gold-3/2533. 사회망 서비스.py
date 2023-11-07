import sys

sys.setrecursionlimit(10**6)

def check_early(node):
    global answer
    check[node] = 1
    for friend in tree[node]:
        if check[friend]:
            continue
        check_early(friend)
        # node가 얼리어답터가 아닐 때 => 자식 노드가 모두 얼리어답터여야 함
        DP[node][0] += DP[friend][1]
        # node가 얼리어답터일 때 => 자식 노드가 얼리어답터이든, 아니든 상관 없음. 더 작은 거 선택
        DP[node][1] += min(DP[friend])

N = int(sys.stdin.readline())

tree = [[] for _ in range(N)]
check = [0]*N
# 얼리어답터 개수 기록
# 0번째 : 내가 얼리어답터가 아닐 때, 1번째 : 내가 얼리어답터일 때
DP = [[0, 1] for _ in range(N)]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

check_early(0)

print(min(DP[0]))