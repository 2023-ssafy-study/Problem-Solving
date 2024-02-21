# 240221
# 31120 KB / 44 ms
S = input()
T = list(input())
len_s, len_t = len(S), len(T)
for _ in range(len_t - len_s):
    last = T.pop()
    if last == 'B':
        T = T[::-1]

print(1 if S == ''.join(T) else 0)


# 31252 KB / 112 ms
S = input()
T = list(input())
len_s, len_t = len(S), len(T)
for i in range(len_t, len_s, -1):
    last = T.pop()
    if last == 'B':
        left, right = 0, i-2
        while left < right:
            T[left], T[right] = T[right], T[left]
            left += 1
            right -= 1

print(1 if S == ''.join(T) else 0)