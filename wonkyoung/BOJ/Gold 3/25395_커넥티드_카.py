# 240702
# 332672 KB / 956 ms (Pypy3)
from collections import deque
def to_int():
    return map(int, input().split())

N, S = to_int()
position = [0] + list(to_int())
fuel_info = [0] + list(to_int())
gap = [0]
for i in range(1, N):
    gap.append(position[i+1] - position[i])

max_fuel = [0] * (N+1)
max_fuel[S] = fuel_info[S]
q = deque()
q.append((S, fuel_info[S]))
candidate = {S}

while q:
    now, fuel = q.popleft()
    if now > 1 and gap[now-1] <= fuel:
        max_val = max(fuel - gap[now-1], fuel_info[now-1])
        if max_val > max_fuel[now-1]:
            q.append((now-1, max_val))
            max_fuel[now - 1] = max_val
            candidate.add(now-1)

    if now < N and gap[now] <= fuel:
        max_val = max(fuel - gap[now], fuel_info[now + 1])
        if max_val > max_fuel[now+1]:
            q.append((now+1, max_val))
            max_fuel[now+1] = max_val
            candidate.add(now+1)

print(*sorted(candidate))


# 332688 KB / 912 ms (Pypy3)
from collections import deque
def to_int():
    return map(int, input().split())

N, S = to_int()
position = [0] + list(to_int())
fuel_info = [0] + list(to_int())
gap = [0]
for i in range(1, N):
    gap.append(position[i+1] - position[i])

max_fuel = [0] * (N+1)
max_fuel[S] = fuel_info[S]
q = deque()
q.append((S))
candidate = {S}
first_i = last_i = S

while q:
    now = q.popleft()
    fuel = max_fuel[now]
    if now > 1 and gap[now-1] <= fuel:
        max_val = max(fuel - gap[now-1], fuel_info[now-1])
        if max_val > max_fuel[now-1]:
            q.append((now-1))
            max_fuel[now - 1] = max_val
            candidate.add(now-1)

    if now < N and gap[now] <= fuel:
        max_val = max(fuel - gap[now], fuel_info[now + 1])
        if max_val > max_fuel[now+1]:
            q.append((now+1))
            max_fuel[now+1] = max_val
            candidate.add(now+1)

print(*sorted(candidate))




# 332680 KB / 1112 ms (Pypy3)
from collections import deque
def to_int():
    return map(int, input().split())

N, S = to_int()
position = [0] + list(to_int())
fuel_info = [0] + list(to_int())
gap = [0]
for i in range(1, N):
    gap.append(position[i+1] - position[i])

max_fuel = [0] * (N+1)
max_fuel[S] = fuel_info[S]
q = deque([S])
candidate = {S}

def renew_fuel(idx1, idx2):
    max_val = max(fuel - gap[idx2], fuel_info[idx1])
    if max_val > max_fuel[idx1]:
        q.append(idx1)
        max_fuel[idx1] = max_val
        candidate.add(idx1)

while q:
    now = q.popleft()
    fuel = max_fuel[now]
    if now > 1 and gap[now-1] <= fuel:
        renew_fuel(now-1, now-1)

    if now < N and gap[now] <= fuel:
        renew_fuel(now+1, now)

print(*sorted(candidate))



# 332680 KB /912 ms (Pypy3)
from collections import deque
def to_int():
    return map(int, input().split())

N, S = to_int()
position = [0] + list(to_int())
fuel_info = [0] + list(to_int())
gap = [0]
for i in range(1, N):
    gap.append(position[i+1] - position[i])

max_fuel = [0] * (N+1)
max_fuel[S] = fuel_info[S]
q = deque([S])
candidate = {S}

def renew_fuel(fuel, idx1, idx2):
    max_val = max(fuel - gap[idx2], fuel_info[idx1])
    if max_val > max_fuel[idx1]:
        q.append(idx1)
        max_fuel[idx1] = max_val
        candidate.add(idx1)

while q:
    now = q.popleft()
    fuel = max_fuel[now]
    if now > 1 and gap[now-1] <= fuel:
        renew_fuel(fuel, now-1, now-1)

    if now < N and gap[now] <= fuel:
        renew_fuel(fuel, now+1, now)

print(*sorted(candidate))



# 332684 KB /1024 ms (Pypy3)
def main():
    from collections import deque

    def to_int():
        return map(int, input().split())

    N, S = to_int()
    position = [0] + list(to_int())
    fuel_info = [0] + list(to_int())
    gap = [0]
    for i in range(1, N):
        gap.append(position[i+1] - position[i])

    max_fuel = [0] * (N+1)
    max_fuel[S] = fuel_info[S]
    q = deque([S])
    candidate = {S}

    def renew_fuel(fuel, idx1, idx2):
        max_val = max(fuel - gap[idx2], fuel_info[idx1])
        if max_val > max_fuel[idx1]:
            q.append(idx1)
            max_fuel[idx1] = max_val
            candidate.add(idx1)

    def bfs():
        while q:
            now = q.popleft()
            fuel = max_fuel[now]
            if now > 1 and gap[now-1] <= fuel:
                renew_fuel(fuel, now-1, now-1)

            if now < N and gap[now] <= fuel:
                renew_fuel(fuel, now+1, now)

    bfs()

    print(*sorted(candidate))

main()
