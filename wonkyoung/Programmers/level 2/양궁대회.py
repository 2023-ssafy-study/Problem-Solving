# 240614
def solution(n, info):
    # 화살 개수, 어피치가 맞힌 과녁 점수 개수
    # 가장 큰 점수 차이로 이겨야 함 -> 여러 가지일 경우 가장 낮은 점수 많이 맞
    path, answer = [0] * 11, [0] * 11
    max_score = 0

    def return_new_score(cnt1, cnt2, ref, idx):
        if cnt1 == cnt2 == 0:
            return ref
        elif cnt1 < cnt2:
            return ref + idx

        return ref - idx

    def dfs(level, total_cnt, score):
        nonlocal max_score
        if level == 10:
            if score > max_score:
                max_score = score
                answer[-1] = n - total_cnt
                for i in range(10):
                    answer[i] = path[i]

            elif score == max_score:
                path[-1] = n - total_cnt
                for i in range(10, -1, -1):
                    if answer[i] > path[i]:
                        return
                    elif answer[i] < path[i]:
                        for i in range(11):
                            answer[i] = path[i]
                        return

            return

        for i in range(n - total_cnt, -1, -1):
            new_score = return_new_score(info[level], i, score, 10 - level)

            path[level] = i
            dfs(level + 1, total_cnt + i, new_score)

    dfs(0, 0, 0)

    return answer if max_score > 0 else [-1]