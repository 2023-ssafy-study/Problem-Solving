N, r, c = map(int, input().split())
answer = 0

while N:
    N -= 1
    pow = 2 ** N

    # 네 부분 중 어디에 속하는지 확인 후 연산
    if r < pow and c < pow:  # 좌측 상단
        answer += pow * pow * 0
    elif r < pow and c >= pow:  # 우측 상단
        answer += pow * pow * 1
        c -= pow
    elif r >= pow and c < pow:  # 좌측 하단
        answer += pow * pow * 2
        r -= pow
    else:  # 우측 하단
        answer += pow * pow * 3
        r -= pow
        c -= pow

print(answer)
