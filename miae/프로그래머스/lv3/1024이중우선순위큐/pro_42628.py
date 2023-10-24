from heapq import heappop, heappush
def solution(operations):
    answer = []
    h = []
    for op in operations:
        o, n = op.split()
        if o == 'I':
            # 이러면 최소값찾는
            heappush(h, int(n))
        else:
            if n == '-1':
                if h:
                    heappop(h)
            else:
                if h:
                    h.pop()
    if h:
        answer = [max(h), min(h)]
    else:
        answer = [0, 0]
    return answer