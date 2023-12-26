N = int(input())
nums = sorted(map(int, input().split()))

answer = 0
for i in range(N):
    l, r = 0, N - 1
    target = nums[i]
    while l < r:
        tmp = nums[l] + nums[r]
        if tmp < target or l == i:
            l += 1
        elif tmp > target or r == i:
            r -= 1
        else:
            answer += 1
            break

print(answer)
