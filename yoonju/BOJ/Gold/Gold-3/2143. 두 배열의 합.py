T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

Adict = {}
Bdict = {}

for left in range(N):
    s = 0
    for right in range(left, N):
        s += A[right]
        if Adict.get(s):
            Adict[s] += 1
        else:
            Adict[s] = 1

for left in range(M):
    s = 0
    for right in range(left, M):
        s += B[right]
        if Bdict.get(s):
            Bdict[s] += 1
        else:
            Bdict[s] = 1

ans = 0

for a in Adict:
    if Bdict.get(T-a):
        ans += Bdict[T-a]*Adict[a]
print(ans)