# 231205
# 31120 KB / 40 ms
N = int(input())
if N == 1:
    print('m')
elif N <= 3:
    print('o')
else:
    k, cnt = 0, 3

    while True:
        if N <= cnt:
            break
        k += 1
        cnt += cnt + k + 3

    def return_moo(level, length, before_cnt):
        if level == 0:
            if length == 1:
                return 'm'
            else:
                return 'o'

        if length < before_cnt+1:
            return return_moo(level - 1, length, (before_cnt - level - 2) // 2)
        elif length == before_cnt+1:
            return 'm'
        elif length < before_cnt + level+3:
            return 'o'

        return return_moo(level-1, length - (before_cnt + level+3), (before_cnt - level - 2)//2)

    print(return_moo(k, N, (cnt - k - 3)//2))


# 31120 KB / 40 ms
N = int(input())
if N == 1:
    print('m')
elif N <= 3:
    print('o')
else:
    k, cnt = 3, 3

    while True:
        if N <= cnt:
            break
        k += 1
        cnt += cnt + k

    def return_moo(level, length, before_cnt):
        if level == 3:
            if length == 1:
                return 'm'
            else:
                return 'o'

        if length < before_cnt+1:
            return return_moo(level - 1, length, (before_cnt - level + 1) // 2)
        elif length == before_cnt+1:
            return 'm'
        elif length < before_cnt + level:
            return 'o'

        return return_moo(level-1, length - (before_cnt + level), (before_cnt - level + 1)//2)

    print(return_moo(k, N, (cnt - k)//2))
