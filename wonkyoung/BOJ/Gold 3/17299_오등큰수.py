#231013
# 155572 KB / 1760 ms
N = int(input()) # 수열 길이
numbers = list(map(int, input().split())) # 수열
frequency = {} # 숫자별 등장 횟수
for number in numbers:
    if frequency.get(number):
        frequency[number] += 1
    else:
        frequency[number] = 1

answer = [-1] * N
stack = numbers[-1:] # 빈도 수 크기 역순으로 정렬할 스택
for i in range(N-2, -1, -1):
    number = numbers[i]
    # 현재 숫자의 빈도 수보다 빈도 수가 큰 수가 나올 때까지 pop
    while frequency[number] >= frequency[stack[-1]]:
        stack.pop()
        # stack이 비면 break (answer 값은 -1)
        if not stack:
            break
    else:
        answer[i] = stack[-1]

    stack.append(number)

print(*answer)


# 155556 KB / 1344 ms
N = int(input()) # 수열 길이
numbers = list(map(int, input().split())) # 수열
frequency = [0] * (int(1e6) + 1) # 숫자별 등장 횟수
for number in numbers:
    frequency[number] += 1

answer = [-1] * N
stack = numbers[-1:] # 빈도 수 크기 역순으로 정렬할 스택
for i in range(N-2, -1, -1):
    number = numbers[i]
    # 현재 숫자의 빈도 수보다 빈도 수가 큰 수가 나올 때까지 pop
    while frequency[number] >= frequency[stack[-1]]:
        stack.pop()
        # stack이 비면 break (answer 값은 -1)
        if not stack:
            break
    else:
        answer[i] = stack[-1]

    stack.append(number)

print(*answer)


# 163128 KB / 840 ms (Python 3)
# 247848 KB / 552 ms (PyPy3)
def find_answer():
    N = int(input()) # 수열 길이
    numbers = list(map(int, input().split())) # 수열
    frequency = [0] * (int(1e6) + 1) # 숫자별 등장 횟수
    for number in numbers:
        frequency[number] += 1

    answer = ['-1'] * N
    stack = numbers[-1:] # 빈도 수 크기 역순으로 정렬할 스택
    for i in range(N-2, -1, -1):
        number = numbers[i]
        # 현재 숫자의 빈도 수보다 빈도 수가 큰 수가 나올 때까지 pop
        while frequency[number] >= frequency[stack[-1]]:
            stack.pop()
            # stack이 비면 break (answer 값은 -1)
            if not stack:
                break
        else:
            answer[i] = str(stack[-1])

        stack.append(number)

    return ' '.join(answer)

print(find_answer())