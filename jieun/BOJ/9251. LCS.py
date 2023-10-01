wa = input()
wb = input()
lengths = [[0] * (len(wb) + 1) for _ in range(len(wa) + 1)]

for i in range(1, len(wa) + 1):
    for j in range(1, len(wb) + 1):
        if wa[i - 1] != wb[j - 1]:
            lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
        else:
            lengths[i][j] = lengths[i - 1][j - 1] + 1

print(lengths[-1][-1])
