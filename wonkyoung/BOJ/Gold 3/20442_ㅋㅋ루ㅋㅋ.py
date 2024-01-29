# 240129
# 37560 KB / 1280 ms
munjayeol = input()
N = len(munjayeol)
if N == 1:
    print(0 if munjayeol == 'K' else 1)
else:
    max_len = r_cnt = munjayeol.count('R')
    left, right = 0, N-1
    left_k_cnt = right_k_cnt = 0

    while True:
        while munjayeol[left] == 'K':
            left_k_cnt += 1
            left += 1
            if left == N:
                break

        while munjayeol[right] == 'K':
            right_k_cnt += 1
            right -= 1
            if right == 0:
                break

        if left <= right:
            now_len = r_cnt
            if left_k_cnt <= right_k_cnt:
                now_len += 2*left_k_cnt
                left += 1
            else:
                now_len += 2*right_k_cnt
                right -= 1

            r_cnt -= 1

            if now_len > max_len:
                max_len = now_len

        else:
            break

    print(max_len)


# 37560 KB / 560 ms (Python) // 120200 KB / 260 ms (Pypy3)
def cnt_len(munjayeol):
    if munjayeol == 'K':
        return 0
    if munjayeol == 'R':
        return 1

    N = len(munjayeol)
    max_len = r_cnt = munjayeol.count('R')
    left, right = 0, N-1
    left_k_cnt = right_k_cnt = 0

    while True:
        while munjayeol[left] == 'K':
            left_k_cnt += 1
            left += 1
            if left == N:
                return max_len

        while munjayeol[right] == 'K':
            right_k_cnt += 1
            right -= 1
            if right == 0:
                return max_len

        if left <= right:
            now_len = r_cnt
            if left_k_cnt <= right_k_cnt:
                now_len += 2*left_k_cnt
                left += 1
            else:
                now_len += 2*right_k_cnt
                right -= 1

            r_cnt -= 1

            if now_len > max_len:
                max_len = now_len

        else:
            return max_len


print(cnt_len(input()))