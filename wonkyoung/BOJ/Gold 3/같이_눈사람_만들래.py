# 240716
# 31120 KB / 7748 ms
N = int(input())
snowballs = sorted(map(int, input().split()))

def find_min_dif():
    min_dif = 2e9
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                total = snowballs[j] + snowballs[k]
                target = total - snowballs[i]
                start, end = k+1, N-1
                while start <= end:
                    mid = (start + end)//2
                    if snowballs[mid] < target:
                        start = mid + 1
                    elif snowballs[mid] > target:
                        end = mid - 1
                    else:
                        return 0
                if k+1 <= start <= N-1 and min_dif > snowballs[start] - target:
                    min_dif = snowballs[start] - target
                if k+1 <= end <= N-1 and min_dif > target - snowballs[end]:
                    min_dif = target - snowballs[end]
    
    return min_dif

print(find_min_dif())


# 31120 KB / 6796 ms
def find_min_dif():
    N = int(input())
    snowballs = sorted(map(int, input().split()))
    min_dif = 2e9
    
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                total = snowballs[j] + snowballs[k]
                target = total - snowballs[i]
                start, end = k+1, N-1
                while start <= end:
                    mid = (start + end)//2
                    if snowballs[mid] < target:
                        start = mid + 1
                    elif snowballs[mid] > target:
                        end = mid - 1
                    else:
                        return 0
                if k+1 <= start <= N-1 and min_dif > snowballs[start] - target:
                    min_dif = snowballs[start] - target
                if k+1 <= end <= N-1 and min_dif > target - snowballs[end]:
                    min_dif = target - snowballs[end]

    return min_dif

print(find_min_dif())




# 110592 KB / 628 ms
def find_min_dif():
    N = int(input())
    snowballs = sorted(map(int, input().split()))
    min_dif = 2e9
    
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                total = snowballs[j] + snowballs[k]
                target = total - snowballs[i]
                start, end = k+1, N-1
                while start <= end:
                    mid = (start + end)//2
                    if snowballs[mid] < target:
                        start = mid + 1
                    elif snowballs[mid] > target:
                        end = mid - 1
                    else:
                        return 0
                if k+1 <= start <= N-1 and min_dif > snowballs[start] - target:
                    min_dif = snowballs[start] - target
                if k+1 <= end <= N-1 and min_dif > target - snowballs[end]:
                    min_dif = target - snowballs[end]

    return min_dif

print(find_min_dif())

