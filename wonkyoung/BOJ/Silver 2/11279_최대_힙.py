# 231023
# 34972 KB / 212 ms
from sys import stdin

def to_int():
    return int(stdin.readline())

N = to_int()
max_heap = [0]
length = 0

def heappush(heap, num):
    heap.append(num)
    child, parent = length, length//2
    while parent and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child, parent = parent, parent//2

def heappop(heap):
    heap[1], heap[-1] = heap[-1], heap[1]
    num = heap.pop()
    parent = 1
    while parent < length:
        left, right = parent*2, parent*2+1
        if left > length:
            break
        elif right > length:
            child = left
        else:
            child = right if heap[right] > heap[left] else left

        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
        else:
            break

    return num


for _ in range(N):
    num = to_int()
    if num:
        length += 1
        heappush(max_heap, num)
    elif length:
        length -= 1
        print(heappop(max_heap))
    else:
        print(0)



# 34972 KB / 184 ms
def print_pop_num():
    from sys import stdin

    def to_int():
        return int(stdin.readline())

    def heappush(heap, num):
        heap.append(num)
        child, parent = length, length//2
        while parent and heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child, parent = parent, parent//2

    def heappop(heap):
        heap[1], heap[-1] = heap[-1], heap[1]
        num = heap.pop()
        parent = 1
        while parent < length:
            left, right = parent*2, parent*2+1
            if left > length:
                break
            elif right > length:
                child = left
            else:
                child = right if heap[right] > heap[left] else left

            if heap[parent] < heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                parent = child
            else:
                break

        return num


    N = to_int()
    max_heap = [0]
    length = 0

    for _ in range(N):
        num = to_int()
        if num:
            length += 1
            heappush(max_heap, num)
        elif length:
            length -= 1
            print(heappop(max_heap))
        else:
            print(0)

print_pop_num()