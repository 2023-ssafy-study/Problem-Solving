#230927
from sys import stdin
N = int(stdin.readline())
schedule = [list(map(int, stdin.readline().split())) for _ in range(N)]
schedule.sort(key=lambda date: (date[0], -date[1]))
start, end = schedule[0]
total_area, height = 0, 1
table = [[False] * 366 for _ in range(N)]

for i in range(start, end+1):
    table[0][i] = True

for i in range(1, N):
    new_start, new_end = schedule[i]
    if new_start <= end+1:
        for j in range(height):
            if not table[j][new_start]:
                for k in range(new_start, new_end+1):
                    table[j][k] = True
                break
        else:
            for k in range(new_start, new_end + 1):
                table[height][k] = True
            height += 1

        if new_end > end:
            end = new_end

    else:
        total_area += (end - start + 1) * height
        for j in range(new_start, new_end + 1):
            table[0][j] = True
        height = 1
        start, end = new_start, new_end
    i += 1

total_area += (end - start + 1) * height

print(total_area)


#
from sys import stdin
N = int(stdin.readline())
schedule = [list(map(int, stdin.readline().split())) for _ in range(N)]
schedule.sort(key=lambda date: (date[0], -date[1]))
start, end = schedule[0]
total_area, height = 0, 1
table = [[] for _ in range(N)]
table[0] = [start, end]

for i in range(1, N):
    new_start, new_end = schedule[i]
    if new_start <= end+1:
        for j in range(height):
            if table[j][1] < new_start:
                table[j][1] = new_end
                break
        else:
            table[height] = [new_start, new_end]
            height += 1

        if new_end > end:
            end = new_end

    else:
        total_area += (end - start + 1) * height
        for j in range(1, height):
            table[j] = []
        height = 1
        start, end = new_start, new_end
        table[0] = [start, end]
    i += 1

total_area += (end - start + 1) * height

print(total_area)


#
def find_area():
    from sys import stdin
    N = int(stdin.readline())

    schedule = [list(map(int, stdin.readline().split())) for _ in range(N)]
    schedule.sort(key=lambda date: (date[0], -date[1]))

    start, end = schedule[0]
    total_area, height = 0, 1
    table = [[] for _ in range(N)]
    table[0] = [start, end]

    for i in range(1, N):
        new_start, new_end = schedule[i]
        if new_start <= end+1:
            for j in range(height):
                if table[j][1] < new_start:
                    table[j][1] = new_end
                    break
            else:
                table[height] = [new_start, new_end]
                height += 1

            if new_end > end:
                end = new_end

        else:
            total_area += (end - start + 1) * height

            table[0] = [new_start, new_end]
            for j in range(1, height):
                table[j] = []

            height = 1
            start, end = new_start, new_end

        i += 1

    total_area += (end - start + 1) * height

    return total_area

print(find_area())

