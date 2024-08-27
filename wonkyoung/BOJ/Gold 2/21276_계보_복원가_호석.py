# 240820
# 69700 KB / 2548 ms
def restore():
    from sys import stdin
    from collections import deque, defaultdict

    new_input = stdin.readline

    N = int(new_input())
    relation, cnt_ancients = defaultdict(list), defaultdict(int)
    for person in new_input().split():
        relation[person] = []
        cnt_ancients[person] = 0

    M = int(input())
    for _ in range(M):
        x, y = new_input().split()
        relation[y] = relation.get(y, []) + [x]
        cnt_ancients[x] += 1
        cnt_ancients[y] = cnt_ancients[y]

    cnt = 0
    roots = []
    children = {}

    for person in cnt_ancients:
        children[person] = []
        if cnt_ancients[person] == 0:
            cnt += 1
            roots.append(person)

    q = deque(roots)

    while q:
        person = q.popleft()
        for new_person in relation[person]:
            cnt_ancients[new_person] -= 1
            if cnt_ancients[new_person] == 0:
                q.append(new_person)
                children[person].append(new_person)


    print(cnt)
    print(*sorted(roots))
    for person in sorted(children):
        print(person, len(children[person]), *sorted(children[person]))


restore()




# 67864 KB / 496 ms
def restore():
    from sys import stdin
    from collections import deque, defaultdict

    new_input = stdin.readline

    N = int(new_input())
    relation, cnt_ancients = defaultdict(list), defaultdict(int)
    for person in new_input().split():
        relation[person] = []
        cnt_ancients[person] = 0

    M = int(input())
    for _ in range(M):
        x, y = new_input().split()
        relation[y].append(x)
        cnt_ancients[x] += 1
        cnt_ancients[y] = cnt_ancients[y]

    cnt = 0
    roots = []
    children = {}

    for person in cnt_ancients:
        children[person] = []
        if cnt_ancients[person] == 0:
            cnt += 1
            roots.append(person)

    q = deque(roots)

    while q:
        person = q.popleft()
        for new_person in relation[person]:
            cnt_ancients[new_person] -= 1
            if cnt_ancients[new_person] == 0:
                q.append(new_person)
                children[person].append(new_person)


    print(cnt)
    print(*sorted(roots))
    for person in sorted(children):
        print(person, len(children[person]), *sorted(children[person]))


restore()
