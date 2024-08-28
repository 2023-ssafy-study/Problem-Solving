# 240828
# 64376 KB / 360 ms
def main():
    from sys import stdin
    def int_input():
        return map(int, stdin.readline().split())

    N, E = int_input()
    road = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, c = int_input()
        road[a].append((c, b))
        road[b].append((c, a))

    u, v = int_input()
    limit = 2e8
    def dijkstra(start):
        from heapq import heappush, heappop
        short_distance = [limit] * (N+1)
        short_distance[start] = 0
        heap = [(0, start)]

        while heap:
            gap, end = heappop(heap)
            if short_distance[end] < gap:
                continue

            for distance, new_end in road[end]:
                new_gap = gap + distance
                if short_distance[new_end] > new_gap:
                    short_distance[new_end] = new_gap
                    heappush(heap, (new_gap, new_end))

        return short_distance

    one_to_other = dijkstra(1)
    u_to_other = dijkstra(u)
    v_to_other = dijkstra(v)

    short_path1 = one_to_other[u] + u_to_other[v] + v_to_other[N]
    short_path2 = one_to_other[v] + v_to_other[u] + u_to_other[N]
    result = min(short_path1, short_path2)

    if result < limit:
        return result
    return -1


print(main())


# 64868 KB / 308 ms
def main():
    from sys import stdin
    def int_input():
        return map(int, stdin.readline().split())

    N, E = int_input()
    road = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, c = int_input()
        road[a].append((c, b))
        road[b].append((c, a))

    u, v = int_input()
    limit = 2e8
    def dijkstra(start, left, right):
        from heapq import heappush, heappop
        short_distance = [limit] * (N+1)
        short_distance[start] = 0
        heap = [(0, start)]

        while heap:
            gap, end = heappop(heap)
            if short_distance[end] < gap:
                continue

            for distance, new_end in road[end]:
                new_gap = gap + distance
                if short_distance[new_end] > new_gap:
                    short_distance[new_end] = new_gap
                    heappush(heap, (new_gap, new_end))

        return (short_distance[left], short_distance[right])

    short_path1 = short_path2 = 0
    for start, left, right in (1, u, v),(u, v, N),(v, N, u):
        val1, val2 = dijkstra(start, left, right)
        short_path1 += val1
        short_path2 += val2

    result = min(short_path1, short_path2)

    if result < limit:
        return result
    
    return -1


print(main())


# 64268 KB / 284 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop
    
    def int_input():
        return map(int, stdin.readline().split())
    
    def fill_road():
        for _ in range(E):
            a, b, c = int_input()
            road[a].append((c, b))
            road[b].append((c, a))

    def dijkstra(start, left, right):
        short_distance = [limit] * (N+1)
        short_distance[start] = 0
        heap = [(0, start)]

        while heap:
            gap, end = heappop(heap)
            if short_distance[end] < gap:
                continue

            for distance, new_end in road[end]:
                new_gap = gap + distance
                if short_distance[new_end] > new_gap:
                    short_distance[new_end] = new_gap
                    heappush(heap, (new_gap, new_end))

        return (short_distance[left], short_distance[right])

    
    def find_short_path():
        short_path1 = short_path2 = 0

        for start, left, right in (1, u, v), (u, v, N), (v, N, u):
            val1, val2 = dijkstra(start, left, right)
            short_path1 += val1
            short_path2 += val2

        result = min(short_path1, short_path2)

        if result < limit:
            return result

        return -1
    
    
    N, E = int_input()
    road = [[] for _ in range(N+1)]
    fill_road()
    
    u, v = int_input()
    limit = 2e8
    
    return find_short_path()

print(main())

