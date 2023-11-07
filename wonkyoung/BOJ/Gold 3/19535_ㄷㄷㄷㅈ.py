# 231107
# 79012 KB / 716 ms
from sys import stdin
N = int(stdin.readline())
link_info = []
degree = [0] * (N+1)
for _ in range(N-1):
    node1, node2 = map(int, stdin.readline().split())
    degree[node1] += 1
    degree[node2] += 1
    link_info.append([node1, node2])

d_cnt = g_cnt = 0
for i in range(1, N+1):
    g_cnt += (degree[i] * (degree[i]-1) * (degree[i]-2)) // 6

for i in range(N-1):
    node1, node2 = link_info[i]
    d_cnt += (degree[node1] - 1) * (degree[node2] - 1)

if d_cnt > 3*g_cnt:
    print('D')
elif d_cnt < 3*g_cnt:
    print('G')
else:
    print('DUDUDUNGA')


# 79012 KB / 528 ms
def find_type():
    from sys import stdin
    N = int(stdin.readline())
    link_info = []
    degree = [0] * (N + 1)
    for _ in range(N - 1):
        node1, node2 = map(int, stdin.readline().split())
        degree[node1] += 1
        degree[node2] += 1
        link_info.append([node1, node2])

    d_cnt = g_cnt = 0
    for i in range(1, N + 1):
        g_cnt += (degree[i] * (degree[i] - 1) * (degree[i] - 2)) // 6

    for i in range(N - 1):
        node1, node2 = link_info[i]
        d_cnt += (degree[node1] - 1) * (degree[node2] - 1)

    if d_cnt > 3 * g_cnt:
        return 'D'
    elif d_cnt < 3 * g_cnt:
        return 'G'

    return 'DUDUDUNGA'

print(find_type())