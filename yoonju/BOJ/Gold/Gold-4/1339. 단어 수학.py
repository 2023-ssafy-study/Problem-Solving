# 31256 KB 40 ms

import sys

N = int(sys.stdin.readline())

words = [sys.stdin.readline().rstrip() for _ in range(N)]

alp_to_num = {}

for word in words:
    word_len = len(word)
    for idx in range(word_len):
        if word[idx] not in alp_to_num:
            alp_to_num[word[idx]] = 0
        alp_to_num[word[idx]] += 10**(word_len - idx - 1)

num = 9
answer = 0

for value in sorted(alp_to_num.values(), reverse=True):
    answer += value*num
    num -= 1

print(answer)