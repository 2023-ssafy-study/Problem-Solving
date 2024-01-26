# 240124
# 240126
# 42204 KB / 120 ms
N = int(input())
power = list(map(int, input().split()))
left, right, gap = 0, N-1, N-2
max_total = 0

while gap:
    if power[left] < power[right]:
        total = power[left] * gap
        left += 1
    else:
        total = power[right] * gap
        right -= 1

    if max_total < total:
        max_total = total

    gap -= 1

print(max_total)


# 42204 KB / 108 ms
N = int(input())
power = list(map(int, input().split()))
left, right, gap, max_total = 0, N-1, N-2, 0

while gap:
    if power[left] < power[right]:
        total = power[left] * gap
        left += 1
    else:
        total = power[right] * gap
        right -= 1

    if max_total < total:
        max_total = total

    gap -= 1

print(max_total)
