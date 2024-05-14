# 240514
# 38632 KB / 188 ms
N, K = map(int, input().split())
splited_nums = list(input())
answer = []
start, first = 1, splited_nums[0]
for i in range(1, K+1):
    num = splited_nums[i]
    if num > first:
        first, start = num, i+1

cnt = start-1
answer.append(first)

for i in range(start, N):
    num = splited_nums[i]
    while num > answer[-1]:
        if cnt == K:
            answer.extend(splited_nums[i:])
            break
        answer.pop()
        cnt += 1
    else:
        answer.append(num)
        continue
    break

print(''.join(answer[:N-K]))



# 38632 KB / 216 ms
N, K = map(int, input().split())
splited_nums = list(input())
answer, start = splited_nums[:1][:], 1

for i in range(1, K+1):
    num = splited_nums[i]
    if num > answer[-1]:
        answer[-1], start = num, i+1

cnt = start-1

for i in range(start, N):
    num = splited_nums[i]
    while num > answer[-1]:
        if cnt == K:
            answer.extend(splited_nums[i:])
            break
        answer.pop()
        cnt += 1
    else:
        answer.append(num)
        continue
    break

print(''.join(answer[:N-K]))


# 38632 KB / 120 ms
def find_first(splited_nums, K):
    start, first = 1, splited_nums[0]
    for i in range(1, K + 1):
        num = splited_nums[i]
        if num > first:
            first, start = num, i + 1

    return first, start


def fill_answer(answer, start, splited_nums, N, K):
    cnt = start-1

    for i in range(start, N):
        num = splited_nums[i]

        while num > answer[-1]:
            if cnt == K:
                return answer + splited_nums[i:]

            answer.pop()
            cnt += 1

        answer.append(num)

    return answer

def main():
    N, K = map(int, input().split())
    splited_nums = list(input())
    first, start = find_first(splited_nums, K)
    answer = fill_answer([first], start, splited_nums, N, K)

    print(''.join(answer[:N-K]))

main()