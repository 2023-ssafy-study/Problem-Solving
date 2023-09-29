N = int(input())
schedule = {}
for _ in range(N):
    S, E = map(int, input().split())
    for h in range(S, E + 1):
        schedule[h] = schedule.get(h, 0) + 1
schedule = sorted(schedule.items())

time, ans, tmp = 0, 0, []
for t, d in schedule:
    if time != 0 and time + 1 != t:
        ans += max(tmp) * len(tmp)
        tmp = []
    time = t
    tmp.append(d)
print(ans + max(tmp) * len(tmp))
