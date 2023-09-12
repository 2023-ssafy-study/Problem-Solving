def check():
    for c in range(W):
        cnt = 1
        for r in range(1, D):
            if film[r - 1][c] == film[r][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt == K:
                break
        else:
            if cnt < K:
                return False
    return True


def drop(r, drop_cnt):
    global answer
    if check():
        answer = min(answer, drop_cnt)
        return
    if answer < drop_cnt or r == D:
        return

    # 투입하지 않는 경우
    drop(r + 1, drop_cnt)

    # 약품 A를 투입하는 경우
    for c in range(W):
        film[r][c] = '0'
    drop(r + 1, drop_cnt + 1)

    # 약품 B를 투입하는 경우
    for c in range(W):
        film[r][c] = '1'
    drop(r + 1, drop_cnt + 1)

    for c in range(W):
        film[r][c] = film_o[r][c]


T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    film = []
    film_o = []
    for _ in range(D):
        film.append(input().split())
        film_o.append(film[-1][:])
    if K == 1 or check():
        answer = 0
    else:
        answer = D + 1
        drop(0, 0)
    print(f'#{tc + 1} {answer}')
