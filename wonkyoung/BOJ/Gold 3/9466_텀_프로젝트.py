# 231206
# 53184 KB / 4228 ms
T = int(input())

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))
    team = [0] * (N+1) # 0 이면 아직 정해지지 않은 것, -1이면 어느 팀에도 속하지 않은 것, 1이면 속한 팀이 있는 것
    for i in range(1, N+1):
        if i == selected[i]:  # 혼자 하고 싶어할 때
            team[i] = 1
        elif team[i] == 0:
            now = selected[i]
            path = {i}
            while True:
                team_num = team[now]
                if team_num != 0: # 속한 팀 이미 있거나, 아무 팀에도 속하지 않을 때
                    for before in path:
                        team[before] = -1
                    break

                elif now == i: # 사이클
                    for before in path:
                        team[before] = 1
                    break

                elif now in path: # i 포함되지 않는 사이클
                    team[i] = -1
                    break

                else:
                    if now == selected[now]: # 혼자 하고 싶어할 때
                        team[now] = 1
                        for before in path:
                            team[before] = -1
                        break
                    path.add(now)
                    now = selected[now]

    print(team.count(-1))


# 53976 KB / 3932 ms
T = int(input())

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))
    team = [0] * (N+1) # 0 이면 아직 정해지지 않은 것, -1이면 어느 팀에도 속하지 않은 것, 1이면 속한 팀이 있는 것
    cnt = 0
    for i in range(1, N+1):
        if i == selected[i]:  # 혼자 하고 싶어할 때
            team[i] = 1
        elif team[i] == 0:
            now = selected[i]
            path = {i}
            while True:
                team_num = team[now]
                if team_num != 0: # 속한 팀 이미 있거나, 아무 팀에도 속하지 않을 때
                    cnt += len(path)
                    for before in path:
                        team[before] = -1
                    break

                elif now == i: # 사이클
                    for before in path:
                        team[before] = 1
                    break

                elif now in path: # i 포함되지 않는 사이클
                    cnt += 1
                    team[i] = -1
                    break

                else:
                    if now == selected[now]: # 혼자 하고 싶어할 때
                        team[now] = 1
                        cnt += len(path)
                        for before in path:
                            team[before] = -1
                        break
                    path.add(now)
                    now = selected[now]

    print(cnt)


# 53468 KB / 2772 ms
T = int(input())

def cnt_teamless(i):
    global cnt
    now = selected[i]
    path = {i}
    while True:
        team_num = team[now]
        if team_num != 0:  # 속한 팀 이미 있거나, 아무 팀에도 속하지 않을 때
            cnt += len(path)
            for before in path:
                team[before] = -1
            return

        elif now == i:  # 사이클
            for before in path:
                team[before] = 1
            return

        elif now in path:  # i 포함되지 않는 사이클
            cnt += 1
            team[i] = -1
            return

        else:
            if now == selected[now]:  # 혼자 하고 싶어할 때
                team[now] = 1
                cnt += len(path)
                for before in path:
                    team[before] = -1
                return

            path.add(now)
            now = selected[now]

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))
    team = [0] * (N+1) # 0 이면 아직 정해지지 않은 것, -1이면 어느 팀에도 속하지 않은 것, 1이면 속한 팀이 있는 것
    cnt = 0
    for i in range(1, N+1):
        if i == selected[i]:  # 혼자 하고 싶어할 때
            team[i] = 1
        elif team[i] == 0:
            cnt_teamless(i)

    print(cnt)


# 53468 KB / 2872 ms
T = int(input())

def cnt_teamless(i):
    now = selected[i]
    path = {i}
    while True:
        team_num = team[now]
        if team_num != 0:  # 속한 팀 이미 있거나, 아무 팀에도 속하지 않을 때
            for before in path:
                team[before] = -1
            return len(path)

        elif now == i:  # 사이클
            for before in path:
                team[before] = 1
            return 0

        elif now in path:  # i 포함되지 않는 사이클
            team[i] = -1
            return 1

        else:
            if now == selected[now]:  # 혼자 하고 싶어할 때
                team[now] = 1
                for before in path:
                    team[before] = -1
                return len(path)

            path.add(now)
            now = selected[now]

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))
    team = [0] * (N+1) # 0 이면 아직 정해지지 않은 것, -1이면 어느 팀에도 속하지 않은 것, 1이면 속한 팀이 있는 것
    cnt = 0
    for i in range(1, N+1):
        if i == selected[i]:  # 혼자 하고 싶어할 때
            team[i] = 1
        elif team[i] == 0:
            cnt += cnt_teamless(i)

    print(cnt)


# 52672 KB / 2884 ms
T = int(input())

def cnt_teamless(i):
    now = selected[i]
    path = {i}
    while True:
        if visited[now]:  # 속한 팀 이미 있거나, 아무 팀에도 속하지 않을 때
            for before in path:
                visited[before] = True
            return len(path)

        elif now == i:  # 사이클
            for before in path:
                visited[before] = True
            return 0

        elif now in path:  # i 포함되지 않는 사이클
            visited[i] = True
            return 1

        else:
            if now == selected[now]:  # 혼자 하고 싶어할 때
                visited[now] = True
                for before in path:
                    visited[before] = True
                return len(path)

            path.add(now)
            now = selected[now]

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if i == selected[i]:  # 혼자 하고 싶어할 때
            visited[i] = True
        elif not visited[i]:
            cnt += cnt_teamless(i)

    print(cnt)