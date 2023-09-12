N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    l = 1
    visit = {}
    flag = True
    for j in range(1, N):
        if board[i][j-1] == board[i][j]:
            # visit에 없을 때
            if (i, j) in visit:
                l = 0
            else:
                l += 1
        elif board[i][j-1] - board[i][j] == 1:
                l = 1
        elif board[i][j] - board[i][j-1] == 1:
            if l >= L:
                for k in range(1, L+1):
                    if (i, j - k) in visit:
                        flag = False
                        break
                    else:
                        visit[(i, j - k)] = True
                if not flag:
                    break
                l = 1
            else:
                flag = False
                # 못한다
                break
        else:
            flag = False
            break
    l = 1
    if flag:
        for j in range(N-2, -1, -1):
            if board[i][j] == board[i][j+1]:
                if (i, j) in visit:
                    l = 0
                else:
                    l += 1
            elif board[i][j+1] - board[i][j] == 1:
                l = 1
            elif board[i][j] - board[i][j+1] == 1:
                if l >= L:
                    for k in range(1, L+1):
                        if (i, j+k) in visit:
                            flag = False
                            break
                        else:
                            visit[(i, j+k)] = True
                    if not flag:
                        break
                    l = 1
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    if flag:
        cnt += 1

for j in range(N):
    l = 1
    visit = {}
    flag = True
    for i in range(1, N):
        if board[i-1][j] == board[i][j]:
            # visit에 없을 때
            if (i, j) in visit:
                l = 0
            else:
                l += 1
        elif board[i-1][j] - board[i][j] == 1:
                l = 1
        elif board[i][j] - board[i-1][j] == 1:
            if l >= L:
                for k in range(1, L+1):
                    if (i - k, j) in visit:
                        flag = False
                        break
                    else:
                        visit[(i-k, j)] = True
                if not flag:
                    break
                l = 1
            else:
                flag = False
                # 못한다
                break
        else:
            flag = False
            break
    l = 1
    if flag:
        for i in range(N-2, -1, -1):
            if board[i + 1][j] == board[i][j]:
            # visit에 없을 때
                if (i, j) in visit:
                    l = 0
                else:
                    l += 1
            elif board[i + 1][j] - board[i][j] == 1:
                l = 1
            elif board[i][j] - board[i + 1][j] == 1:
                if l >= L:
                    for k in range(1, L + 1):
                        if (i + k, j) in visit:
                            flag = False
                            break
                        else:
                            visit[(i + k, j)] = True
                    if not flag:
                        break
                    l = 1
                else:
                    flag = False
                    # 못한다
                    break
            else:
                flag = False
                break
    if flag:
        cnt += 1
print(cnt)