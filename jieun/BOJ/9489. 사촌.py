from collections import defaultdict

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:   break
    arr = tuple(map(int, input().split()))
    tree = defaultdict(int) # key:자식 value:부모

    parent_i = 0
    for i in range(1, n):
        if 1 < i and arr[i] - arr[i - 1] > 1:  # 연속적인지 확인
            parent_i += 1
        tree[arr[i]] = arr[parent_i]

    answer = 0
    if tree[tree[k]]:  # k의 부모의 부모노드가 존재한다면
        for v in arr:
            if tree[tree[k]] == tree[tree[v]] and tree[k] != tree[v]:  # 사촌노드: 부모노드가 다르면서 부모의 부모노드가 같다
                answer += 1
    print(answer)
