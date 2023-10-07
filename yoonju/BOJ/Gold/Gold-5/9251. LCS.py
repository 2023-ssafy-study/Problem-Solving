# 55716 KB 360 ms (python3)

import sys

def find_LCS(first, second):
    DP = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])
    return DP[-1][-1]

first_word = sys.stdin.readline().rstrip()
second_word = sys.stdin.readline().rstrip()

print(find_LCS(first_word, second_word))