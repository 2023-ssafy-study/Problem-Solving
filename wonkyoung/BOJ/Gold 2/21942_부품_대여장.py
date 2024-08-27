# 240827
# 48964 KB / 360 ms
def convert(input_val):
    if input_val.isdigit():
        return int(input_val)
    return tuple(map(int, (input_val[:3], input_val[4:6], input_val[7:])))

def date_to_num(date):
    _, month, result = map(int, date.split('-'))
    for i in range(month):
        if i == 2:
            result += 28
        elif i in {4, 6, 9, 11}:
            result += 30
        else:
            result += 31

    return result

def duration_to_minute(day, hour, minute):
    return (day * 24 + hour) * 60 + minute


def main():
    from sys import stdin
    from collections import defaultdict
    new_input = stdin.readline

    N, (day, hour, minute), F = map(convert, new_input().split())
    limit_m = duration_to_minute(day, hour, minute)
    check = defaultdict(dict)
    penalty = defaultdict(int)

    for _ in range(N):
        date, time, kind_of, name = new_input().split()
        if check.get(name) and check[name].get(kind_of):
            after_num, after_h, after_m = map(int, [date_to_num(date), *time.split(':')])
            before_num, before_h, before_m = check[name][kind_of]
            delay = duration_to_minute(after_num - before_num, after_h-before_h, after_m-before_m) - limit_m
            if delay > 0:
                penalty[name] += delay * F
            del check[name][kind_of]
        else:
            check[name][kind_of] = tuple(map(int, [date_to_num(date), *time.split(':')]))

    if penalty:
        for name in sorted(penalty):
            print(name, penalty[name])
    else:
        print(-1)

main()
