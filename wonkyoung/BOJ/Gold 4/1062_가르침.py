# 240422
# 31120 KB / 1248 ms
N, K = map(int, input().split())
if K < 5: # anta, tica 만족 X
    print(0)
else:
    alp_to_num = {} # alphabet: bitmask
    converted_words = [] # [bitmask, ...]
    candidates = set()
    already = set('antic')

    num, a_num = 1, ord('a')
    for i in range(26):
        alp_to_num[chr(a_num+i)] = num
        num *= 2

    max_cnt = state = 0
    for alp in already:
        state += alp_to_num[alp]

    def choose_alp(level, ref, start):
        global max_cnt
        if max_cnt == N:
            return

        if level == K:
            cnt = 0
            for j in range(N):
                word_state = converted_words[j]
                if ref & word_state == word_state:
                    cnt += 1

            if cnt > max_cnt:
                max_cnt = cnt
            return

        for i in range(start, M):
            num = alp_to_num[candidates[i]]
            choose_alp(level+1, ref|num, i+1)

    for _ in range(N):
        word_set = set(input()[4:-4]) - already

        new_state = state
        for alp in word_set:
            new_state += alp_to_num[alp]

        converted_words.append(new_state)
        candidates.update(word_set)

    M = len(candidates)
    K = min(K, M+5)
    candidates = list(candidates)
    choose_alp(5, state, 0)

    print(max_cnt)


