# 240513
# 49748 KB / 292 ms
N = int(input())
height_list = list(map(int, input().split()))
stack = [(height_list[0], 0)]
cnt_list, nearest_building = [0] * N, [-1] * N

# 자신보다 작은 번호
for i in range(1, N):
    height = height_list[i]
    while height >= stack[-1][0]:
        stack.pop()
        if not stack:
            break
    else:
        cnt_list[i] += len(stack)
        nearest_building[i] = stack[-1][1]

    stack.append((height, i))

# 자신보다 큰 번호
stack = [(height_list[-1], N-1)]
for i in range(N-2, -1, -1):
    height = height_list[i]
    while height >= stack[-1][0]:
        stack.pop()
        if not stack:
            break
    else:
        cnt_list[i] += len(stack)
        before, new = nearest_building[i], stack[-1][1]
        if before == -1:
            nearest_building[i] = new
        elif abs(i - before) > abs(new - i):
            nearest_building[i] = new

    stack.append((height, i))

for i in range(N):
    if cnt_list[i] == 0:
        print(0)
    else:
        print(cnt_list[i], nearest_building[i]+1)


# 49748 KB / 292 ms
N = int(input())
height_list = list(map(int, input().split()))
stack = [(height_list[0], 0)]
cnt_list, nearest_building = [0] * N, [-1] * N

# 자신보다 작은 번호
for i in range(1, N):
    height = height_list[i]
    while height >= stack[-1][0]:
        stack.pop()
        if not stack:
            break
    else:
        cnt_list[i] += len(stack)
        nearest_building[i] = stack[-1][1]

    stack.append((height, i))

# 자신보다 큰 번호
stack = [(height_list[-1], N-1)]
for i in range(N-2, -1, -1):
    height = height_list[i]
    while height >= stack[-1][0]:
        stack.pop()
        if not stack:
            break
    else:
        cnt_list[i] += len(stack)
        before, new = nearest_building[i], stack[-1][1]
        if before == -1:
            nearest_building[i] = new
        elif i - before > new - i:
            nearest_building[i] = new

    stack.append((height, i))

for i in range(N):
    if cnt_list[i] == 0:
        print(0)
    else:
        print(cnt_list[i], nearest_building[i]+1)



# 49644 KB / 300 ms
N = int(input())
height_list = list(map(int, input().split()))
cnt_list, nearest_building = [0] * N, [-1] * N

for start, end, step in (0, N, 1), (N-1, -1, -1):
    stack = [(height_list[start], start)]
    for i in range(start+step, end, step):
        height = height_list[i]
        while height >= stack[-1][0]:
            stack.pop()
            if not stack:
                break
        else:
            cnt_list[i] += len(stack)
            before, new = nearest_building[i], stack[-1][1]
            if before == -1:
                nearest_building[i] = new
            elif i - before > new - i:
                nearest_building[i] = new

        stack.append((height, i))

for i in range(N):
    if cnt_list[i] == 0:
        print(0)
    else:
        print(cnt_list[i], nearest_building[i]+1)


# 49644 KB / 288 ms
N = int(input())
height_list = list(map(int, input().split()))
cnt_list, nearest_building = [0] * N, [-1] * N

for start, end, step in (0, N, 1), (N-1, -1, -1):
    stack = [(height_list[start], start)]
    length = 1
    for i in range(start+step, end, step):
        height = height_list[i]
        while height >= stack[-1][0]:
            stack.pop()
            length -= 1
            if not stack:
                break
        else:
            cnt_list[i] += length
            before, new = nearest_building[i], stack[-1][1]
            if before == -1:
                nearest_building[i] = new
            elif i - before > new - i:
                nearest_building[i] = new

        stack.append((height, i))
        length += 1

for i in range(N):
    if cnt_list[i] == 0:
        print(0)
    else:
        print(cnt_list[i], nearest_building[i]+1)