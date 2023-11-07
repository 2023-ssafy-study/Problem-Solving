import sys

def find_siblings(nodes, len, target):
    target_idx = 0
    parents = [-1]*len
    p_index = -1
    answer = 0

    for idx in range(1, len):
        # 찾아야 하는 수의 index 저장
        if nodes[idx] == target:
            target_idx = idx
        # 연속이 아님 => 부모 바뀜
        if nodes[idx] - nodes[idx-1] > 1:
            p_index += 1
        # 부모 지정
        parents[idx] = p_index

    for idx in range(len):
        # 찾아야 하는 수 => 자기 자신이므로 건너뜀
        if idx == target_idx:
            continue
        # 부모가 같음 => 건너뜀
        if parents[idx] == parents[target_idx]:
            continue
        # 부모는 다르지만 조부모는 같음 => +1
        if parents[parents[idx]] == parents[parents[target_idx]]:
            answer += 1

    print(answer)

while True:
    N, K = map(int, sys.stdin.readline().split())
    if N == 0 and K == 0:
        break
    nodes = list(map(int, sys.stdin.readline().split()))

    find_siblings(nodes, N, K)
