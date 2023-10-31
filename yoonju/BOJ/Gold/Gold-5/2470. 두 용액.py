N = int(input())

liq = list(map(int, input().split()))

liq.sort()

s = 0
e = N-1

ans = liq[s]+liq[e]

resL = liq[s]
resR = liq[e]

while s < e:
    temp = liq[s]+liq[e]

    if abs(temp) < abs(ans):
        ans = temp
        resL = liq[s]
        resR = liq[e]

    if temp < 0:
        s += 1
    else:
        e -= 1

print(resL, resR)