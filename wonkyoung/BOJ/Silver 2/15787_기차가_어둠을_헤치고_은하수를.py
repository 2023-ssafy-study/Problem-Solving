# 240709
# 31896 KB / 164 ms

from sys import stdin

def convert(func):
    return map(func, stdin.readline().split())

N, M = convert(int)
train = [0] * N
limit = (1 << 20) - 1
for _ in range(M):
    num, *command = convert(lambda x: int(x)-1)
    if num <= 1:
        idx, seat = command
        if num == 0:
            train[idx] |= (1 << seat)
        else:
            train[idx] &= ~(1 << seat)
    elif num == 2:
        train[command[0]] <<= 1
        train[command[0]] &= limit
    else:
        train[command[0]] >>= 1

print(len(set(train)))
