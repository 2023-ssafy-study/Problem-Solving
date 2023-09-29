# 230912
# 78624 KB / 3323 ms
def cnt_add_chemical():
    D, W, K = map(int, input().split())
    film_info = [input().split() for _ in range(D)]

    def can_pass_test():
        for j in range(W):
            cnt_zero = cnt_one = 0
            for i in range(K - 1):
                if film_info[i][j] == '0':
                    cnt_zero += 1
                    cnt_one = 0
                else:
                    cnt_zero = 0
                    cnt_one += 1

            found = False
            for i in range(K - 1, D):
                if film_info[i][j] == '0':
                    cnt_zero += 1
                    cnt_one = 0
                    if cnt_zero == K:
                        cnt_zero -= 1
                        found = True
                else:
                    cnt_zero = 0
                    cnt_one += 1
                    if cnt_one == K:
                        cnt_one -= 1
                        found = True

            if not found:
                return False

        return True

    if can_pass_test():
        return 0

    def dfs(level, limit, start=0):
        nonlocal possible
        if possible:
            return
        if level == limit:
            if can_pass_test():
                possible = True
            return
        for i in range(start, D):
            for kind_of in ('0', '1'):
                before = film_info[i][:]
                film_info[i] = [kind_of] * W
                dfs(level + 1, limit, i + 1)
                film_info[i] = before[:]

    for i in range(1, K):
        possible = False
        dfs(0, i)
        if possible:
            return i

    return K


T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} {cnt_add_chemical()}')



# 78624 KB / 3138 ms
def cnt_add_chemical():
    D, W, K = map(int, input().split())
    film_info = [input().split() for _ in range(D)]

    def can_pass_test():
        for j in range(W):
            cnt_zero = cnt_one = 0
            for i in range(K - 1):
                if film_info[i][j] == '0':
                    cnt_zero += 1
                    cnt_one = 0
                else:
                    cnt_zero = 0
                    cnt_one += 1

            for i in range(K - 1, D):
                if film_info[i][j] == '0':
                    cnt_zero += 1
                    cnt_one = 0
                    if cnt_zero == K:
                        break
                else:
                    cnt_zero = 0
                    cnt_one += 1
                    if cnt_one == K:
                        break
            else:
                return False

        return True

    if can_pass_test():
        return 0

    def dfs(level, limit, start=0):
        nonlocal possible
        if possible:
            return
        if level == limit:
            if can_pass_test():
                possible = True
            return
        for i in range(start, D):
            for kind_of in ('0', '1'):
                before = film_info[i][:]
                film_info[i] = [kind_of] * W
                dfs(level + 1, limit, i + 1)
                film_info[i] = before[:]

    for i in range(1, K):
        possible = False
        dfs(0, i)
        if possible:
            return i

    return K


T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} {cnt_add_chemical()}')