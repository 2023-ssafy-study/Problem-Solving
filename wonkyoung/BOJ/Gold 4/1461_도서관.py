# 231114
# 31120 KB / 40 ms
N, M = map(int, input().split())
book_list = list(map(int, input().split()))
if N > 1:
    book_list.sort()
    cnt_list = []
    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if book_list[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1
    i = 0
    while i < start:
        cnt_list.append(-book_list[i])
        i += M

    i = N-1
    while i >= start:
        cnt_list.append(book_list[i])
        i -= M

    print(sum(cnt_list)*2 - max(cnt_list))

else:
    print(book_list[0])



# 31120 KB / 44 ms
def min_total():
    N, M = map(int, input().split())
    book_list = list(map(int, input().split()))
    if N == 1:
        return book_list[0]

    book_list.sort()
    cnt_list = []

    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if book_list[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1
    i = 0
    while i < start:
        cnt_list.append(-book_list[i])
        i += M

    i = N-1
    while i >= start:
        cnt_list.append(book_list[i])
        i -= M

    return sum(cnt_list)*2 - max(cnt_list)

print(min_total())