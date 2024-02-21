# 240220
N = int(input())
sound = input()
left = cnt = 0
check = {}
length = len(sound)

for i in range(length):
    alp = sound[i]
    if check.get(alp):
        check[alp] += 1
    elif cnt == N:
        right = max_len = i
        break
    else:
        cnt += 1
        check[alp] = 1

else:
    right = max_len = length

now_len = max_len

while right < length:
    while left < length:
        removed_alp = sound[left]
        now_len -= 1
        check[removed_alp] -= 1
        left += 1
        if check[removed_alp] == 0:
            cnt -= 1
            break

    while right < length:
        alp = sound[right]
        if check.get(alp):
            check[alp] += 1
        elif cnt == N:
            break
        else:
            cnt += 1
            check[alp] = 1

        now_len += 1
        right += 1

    if max_len < now_len:
        max_len = now_len

if max_len < now_len:
    max_len = now_len

print(max_len)
