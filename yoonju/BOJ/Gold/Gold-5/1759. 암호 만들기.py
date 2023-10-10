# 31256 KB 48 ms

import sys

L, C = map(int, sys.stdin.readline().split())

alps = list(sys.stdin.readline().split())

alps.sort()

vowels = ['a', 'e', 'i', 'o', 'u']

def dfs(level, now, password):
    if level == L:
        # 최소 한 개의 모음과 최소 두 개의 자음
        vowel_cnt = 0
        consonant_cnt = 0
        for p in password:
            if p in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(password)
    if level >= L:
        return

    for idx in range(now+1, C):
        dfs(level+1, idx, password + alps[idx])

dfs(0, -1, '')