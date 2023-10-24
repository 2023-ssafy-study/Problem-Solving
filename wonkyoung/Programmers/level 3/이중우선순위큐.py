# 이전
'''
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
'''
def solution(operations):
    from heapq import heappush, heappop, heapify
    q, q2, = [], []
    max_num = ''
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heappush(q, num)
            heappush(q2, -num)
        elif num == 1:
            if q2:
                max_val = heappop(q2)
                q.remove(-max_val)
                heapify(q)
        elif q:
            min_val = heappop(q)
            q2.remove(-min_val)
            heapify(q2)
    if not q:
        return [0, 0]
    max_val = heappop(q2)
    min_val = heappop(q)
    return [-max_val, min_val]


# 231023
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
'''
def solution(operations):
    from heapq import heappush, heappop

    def pop_num(heap, visited):
        while heap:
            num, index = heappop(heap)
            if not visited[index]:
                visited[index] = True
                return num
        return

    max_heap, min_heap = [], []
    length = len(operations)
    visited = [False] * length
    for i in range(length):
        command, data = operations[i].split()
        if command == 'I':
            heappush(max_heap, (-int(data), i))
            heappush(min_heap, (int(data), i))
        elif data == '1':
            num = pop_num(max_heap, visited)
            if num is not None:
                print(-num)
        else:
            num = pop_num(min_heap, visited)
            if num is not None:
                print(-num)

    answer = []
    max_num = pop_num(max_heap, visited)
    answer.append(-max_num if max_num is not None else 0)
    min_num = pop_num(min_heap, visited)
    answer.append(min_num if min_num is not None else 0)

    return answer