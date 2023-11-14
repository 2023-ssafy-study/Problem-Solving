N = int(input())
sum_a = 0  # 전체 주민의 수
XA = []  # (위치, 주민 수)
for i in range(1, N + 1):
    x, a = map(int, input().split())
    sum_a += a
    XA.append((x, a))
XA.sort()

# *주민 수의 절반을 넘는 지점에 우체국을 둔다*
cnt = 0  # 현재 위치까지의 주민 수의 합
for x, a in XA:
    cnt += a
    if cnt >= sum_a / 2:
        print(x)
        break
