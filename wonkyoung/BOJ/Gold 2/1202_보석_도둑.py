# 240429
# 145268 KB / 2700 ms
from sys import stdin
from heapq import heappush, heappop

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end)//2
        if jewels[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end

new_input = stdin.readline
N, K = map(int, new_input().split())
jewels = [list(map(int, new_input().split())) for _ in range(N)]
bags = [int(new_input()) for _ in range(K)]
jewels.sort()
bags.sort()

jewel_values = []

total = 0
before_limit = 0
for bag in bags:
    limit = binary_search(0, N-1, bag)+1
    for i in range(before_limit, limit):
        heappush(jewel_values, (-jewels[i][1], -i))
    if jewel_values:
        minus_val, i = heappop(jewel_values)
        total -= minus_val
    before_limit = limit

print(total)



# 145268 KB / 2908 ms
from sys import stdin
from heapq import heappush, heappop

def binary_search(target):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if jewels[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end

new_input = stdin.readline
N, K = map(int, new_input().split())
jewels = [list(map(int, new_input().split())) for _ in range(N)]
bags = [int(new_input()) for _ in range(K)]
jewels.sort()
bags.sort()

jewel_values = []

total = 0
before_limit = 0
for bag in bags:
    limit = binary_search(bag)+1
    for i in range(before_limit, limit):
        heappush(jewel_values, (-jewels[i][1], -i))
    if jewel_values:
        minus_val, i = heappop(jewel_values)
        total -= minus_val
    before_limit = limit

print(total)


# 116596 KB / 2304 ms
from sys import stdin
from heapq import heappush, heappop

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end)//2
        if jewels[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end

new_input = stdin.readline
N, K = map(int, new_input().split())
jewels = [list(map(int, new_input().split())) for _ in range(N)]
bags = [int(new_input()) for _ in range(K)]
jewels.sort()
bags.sort()

jewel_values = []

total = 0
before_limit = 0
for bag in bags:
    limit = binary_search(0, N-1, bag)+1
    for i in range(before_limit, limit):
        heappush(jewel_values, -jewels[i][1])
    if jewel_values:
        minus_val = heappop(jewel_values)
        total -= minus_val
    before_limit = limit

print(total)




# 116596 KB / 2212 ms
def binary_search(start, end, target, arr):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end

def steal(bags, jewels, N):
    from heapq import heappush, heappop

    jewel_values = []
    total = before_limit = 0

    for bag in bags:
        limit = binary_search(0, N - 1, bag, jewels) + 1

        for i in range(before_limit, limit):
            heappush(jewel_values, -jewels[i][1])

        if jewel_values:
            total -= heappop(jewel_values)

        before_limit = limit

    return total

def main():
    from sys import stdin

    new_input = stdin.readline
    N, K = map(int, new_input().split())
    jewels = [list(map(int, new_input().split())) for _ in range(N)]
    bags = [int(new_input()) for _ in range(K)]
    jewels.sort()
    bags.sort()

    return steal(bags, jewels, N)


print(main())