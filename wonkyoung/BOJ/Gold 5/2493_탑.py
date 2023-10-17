#231017
# 99304 KB / 552 ms
# 현재 탑보다 왼쪽에 있으면서, 높고 가까운 탑 번호 찾기 (없으면 0)
'''
5
6 9 5 7 4
'''
N = int(input()) # 탑의 개수
tower_list = list(map(int, input().split())) # 탑의 높이
received_tower = [0] * N # 레이저 신호 수신한 탑
stack = [0] # 현재 탑의 높이보다 높은 탑의 인덱스
last = 0 # stack의 가장 마지막 값
for i in range(1, N):
    # stack에 있는 탑 중 현재 탑보다 높은 탑 찾기
    while tower_list[i] > tower_list[last]:
        stack.pop()
        if not stack: # 현재 탑의 높이보다 높은 탑이 왼쪽에 없음
            break
        last = stack[-1]
    else:
        received_tower[i] = last+1
    stack.append(i)
    last = i

print(*received_tower)


# 113273 KB / 484 ms
N = int(input()) # 탑의 개수
tower_list = list(map(int, input().split())) # 탑의 높이
received_tower = ['0'] * N # 레이저 신호 수신한 탑
stack = [0] # 현재 탑의 높이보다 높은 탑의 인덱스
last = 0
for i in range(1, N):
    while tower_list[i] > tower_list[last]:
        stack.pop()
        if not stack:
            break
        last = stack[-1]
    else:
        received_tower[i] = str(last+1)
    stack.append(i)
    last = i

print(' '.join(received_tower))


# 109960 KB / 336 ms
def find_received_tower_list():
    N = int(input())  # 탑의 개수
    tower_list = list(map(int, input().split()))  # 탑의 높이
    received_tower = ['0'] * N  # 레이저 신호 수신한 탑
    stack = [0]  # 현재 탑의 높이보다 높은 탑의 인덱스
    last = 0
    for i in range(1, N):
        while tower_list[i] > tower_list[last]:
            stack.pop()
            if not stack:
                break
            last = stack[-1]
        else:
            received_tower[i] = str(last + 1)
        stack.append(i)
        last = i

    return ' '.join(received_tower)

print(find_received_tower_list())


# 89736 KB / 360 ms
def find_received_tower_list():
    N = int(input())  # 탑의 개수
    tower_list = list(map(int, input().split()))  # 탑의 높이
    received_tower = '0'  # 레이저 신호 수신한 탑
    stack = [0]  # 현재 탑의 높이보다 높은 탑의 인덱스
    last = 0
    for i in range(1, N):
        while tower_list[i] > tower_list[last]:
            stack.pop()
            if not stack:
                received_tower += f' 0'
                break
            last = stack[-1]
        else:
            received_tower += f' {last + 1}'
        stack.append(i)
        last = i

    return received_tower

print(find_received_tower_list())



# 89736 KB / 400 ms
def find_received_tower_list():
    N = int(input())  # 탑의 개수
    tower_list = list(map(int, input().split()))  # 탑의 높이

    received_tower = '0'  # 레이저 신호 수신한 탑
    stack = [0]  # 현재 탑의 높이보다 높은 탑의 인덱스

    for i in range(1, N):
        while tower_list[i] > tower_list[stack[-1]]:
            stack.pop()
            if not stack:
                received_tower += f' 0'
                break
        else:
            received_tower += f' {stack[-1] + 1}'

        stack.append(i)

    return received_tower

print(find_received_tower_list())
